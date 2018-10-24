#Installation of the HTML Generating tools and Web Site
This page explains setup of combined build and web app. If you are only
installing one or the other you may skip some steps.

## Prerequisites
1. Go
2. Docker
3. About 10 GB of memory for the build server, much less for only the web app
4. GCS bucket optional for cloud hosting
5. Attached block storage device for cloud hosting

These instructions assume that you will work directly under $HOME. Change
the top level directory if you are working in another location.

## Get the source from GitHub
```
git clone git://github.com/alexamies/buddhist-dictionary
git clone git://github.com/alexamies/chinesenotes.com

```

## Build generated HTML files
```
# Install Go lang

cd chinesenotes.com/go/
source path.bash.inc
cd src/cnreader
go build cnreader
cd $HOME
bin/ntireader.sh
```

## Upload to a GCS bucket
First time setup:
```
export BUCKET={your bucket}
gsutil mb gs://$BUCKET
gsutil web set -m index.html -e 404.html gs://$BUCKET
```

When generating new content
```
bin/push.sh
```

## Database
[Mariadb Documentation](https://mariadb.org/)

The application uses a Mariadb database. 

### Mariadb Docker Image
[Mariadb Image Documentation](https://hub.docker.com/r/library/mariadb/)

### Running locally
To start a Docker container with Mariadb and connect to it from a MySQL command
line client execute the command below. First, set environment variable 
`MYSQL_ROOT_PASSWORD`.

```
docker run --name mariadb -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD -d \
  --mount type=bind,source="$(pwd)"/data,target=/ntidata \
  mariadb:10.3
docker exec -it mariadb bash
mysql --local-infile=1 -h localhost -u root -p
```

The data in the database is persistent unless the container is deleted. To
restart the database use the command

```
docker restart  mariadb
```

To load data from other sources connect to the database container

### Text Files for Full Text Search
Copy the text files to an object store. If you prefer not to use GCS, then you
can use the local file system on the application server. The instructions here
are for GCS. See [Authenticating to Cloud Platform with Service
Accounts](https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform)
for detailed instructions on authentication.

```
TEXT_BUCKET={your txt bucket}
# First time
gsutil mb gs://$TEXT_BUCKET
gsutil -m rsync -d -r corpus gs://$TEXT_BUCKET
```

To enable the web application to access the storage system, create a service
account with a GCS Storage Object Admin role and download the JSOn credentials
file, as described in [Create service account
credentials](https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform).
Assuming that you saved the file in the current working directory as 
credentials.json, create a local environment variable for local testing
```
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/credentials.json
```

go get -u cloud.google.com/go/storage

## Deploying to Production
### Set up a Cloud SQL Database
New: Replacing management of the Mariadb database in a Kubernetes cluster
Follow instructions in 
[Cloud SQL Quickstart](https://cloud.google.com/sql/docs/mysql/quickstart) using
the Cloud Console.

Connect to the instance from the Cloud Shell of a GCE instance
```
cd data
INSTANCE=cnotes
gcloud sql connect $INSTANCE --user=root
```

Execute statements in first_time_setup.sql, data/dictionary/dictionary.ddl, and 
data/corpus/corpus_index.ddl to define the database and tables.

Import the data for table word_freq_doc via the Cloud Console using the import
function. The other tables can be imported using the MySQL client (much faster):
```
#source notes.ddl
#source corpus_index.ddl
#source drop.sql
#source delete_index.sql
source load_data.sql
source load_index.sql
#source data/library/digital_library.sql
```

Load word_freq_doc.txt via GCS
```
cd index
gcloud sql connect $INSTANCE --user=root
source load_word_freq.sql
```

### Set Up Kubernetes Cluster and Deployment
[Container Engine Quickstart](https://cloud.google.com/container-engine/docs/quickstart)
The dynamic part of the app run in a Kubernetes cluster using Google
Kubernetes Engine. To create the cluster and authenticate to it:
```
gcloud container clusters create $CLUSTER \
  --zone=$ZONE \
  --disk-size=500 \
  --machine-type=n1-standard-1 \
  --num-nodes=1 \
  --enable-cloud-monitoring
gcloud container clusters get-credentials $CLUSTER --zone=$ZONE
```

Configure access to Cloud SQL using instructions in
[Connecting from Kubernetes Engine](https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine).
Save the JSON key file. Create the proxy user:

```
PROXY_PASSWORD=[Your value]
gcloud sql users create proxyuser cloudsqlproxy~% --instance=$INSTANCE \
  --password=$PROXY_PASSWORD
```

Get the instance connection name:
```
gcloud sql instances describe $INSTANCE
```

Create secrets
```
PROXY_KEY_FILE_PATH=[JSON file]
kubectl create secret generic cloudsql-instance-credentials \
    --from-file=credentials.json=$PROXY_KEY_FILE_PATH
kubectl create secret generic cloudsql-db-credentials \
    --from-literal=username=proxyuser --from-literal=password=$PROXY_PASSWORD
```

Deploy the app tier
```
kubectl apply -f kubernetes/app-deployment.yaml 
kubectl apply -f kubernetes/app-service.yaml
```

Test from the command line
```
kubectl get pods
POD_NAME=[your pod name]
kubectl exec -it $POD_NAME bash
apt-get update
apt-get install curl
curl http://localhost:8081/find/?query=hello
```

The load balancer connects to the Kubernetes NodePort with a managed instance
group named port. To get the list of named ports use the command
```
gcloud compute instance-groups list
MIG=[your managed instance group]
gcloud compute instance-groups managed get-named-ports $MIG
```

To add a new named port use the command
```
PORTNAME=cnotesport
PORT=30080
gcloud compute instance-groups managed set-named-ports $MIG \
  --named-ports="$PORTNAME:$PORT" \
  --zone=$ZONE
```
Be careful with this command that you do not accidentally clear the already
existing named ports that other apps in the cluster may be depending on.

### Create and configure the load balancer

Configure a load balancer that will direct HTTP requests to the backend bucket
and Kubernetes service based on path. Use these commands, setting the values for
INSTANCE_GROUP and HOST appropriately for your installation:
```
INSTANCE_GROUP=[Your value]
HOST=[Your value]
gcloud compute firewall-rules create ntireader-app-rule \
    --allow tcp:30081 \
    --source-ranges 130.211.0.0/22,35.191.0.0/16
gcloud compute health-checks create http ntireader-app-check --port=30081 \
     --request-path=/healthcheck/
gcloud compute backend-services create ntireader-service \
     --protocol HTTP \
     --health-checks ntireader-app-check \
     --global
gcloud compute backend-services add-backend ntireader-service \
    --balancing-mode UTILIZATION \
    --max-utilization 0.8 \
    --capacity-scaler 1 \
    --instance-group $INSTANCE_GROUP \
    --instance-group-zone $ZONE \
    --global
gcloud compute backend-buckets create ntireader-web-bucket --gcs-bucket-name $BUCKET
gcloud compute url-maps create ntireader-map \
    --default-backend-bucket ntireader-web-bucket
gcloud compute url-maps add-path-matcher ntireader-map \
    --default-backend-bucket ntireader-web-bucket \
    --path-matcher-name ntinreader-matcher \
    --path-rules="/find/*=ntireader-service,/findadvanced/*=$BACKEND_NAME,/findmedia/*=ntireader-service" \
    --new-hosts=$HOST
gcloud compute target-http-proxies create ntireader-lb-proxy \
    --url-map ntireader-map
gcloud compute addresses create ntireader-web --global
gcloud compute forwarding-rules create ntireader-content-rule \
    --address ntireader-web \
    --global \
    --target-http-proxy ntireader-lb-proxy \
    --ports 80
```

Also, check the named port on the instance group.