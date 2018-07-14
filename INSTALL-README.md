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

### Running on Kubernetes
Set up the mariadb software as per the [Chinese Notes instructions](https://github.com/alexamies/chinesenotes.com).
```
gcloud container clusters get-credentials $CLUSTER --zone=$ZONE
```


The first time Configure the database check first_time_setup.sql and execute
```
source dictionary/dictionary.ddl
source corpus/corpus_index.ddl

```

After first time setup, follow the commands below, setting your own value for 
POD_NAME.

```
kubectl get pods
POD_NAME=
tar -zcf  ntidata.tar.gz data
kubectl cp ntidata.tar.gz $POD_NAME:.
kubectl exec -it $POD_NAME bash
rm -rf data
rm -rf ntidata/*
tar -zxf ntidata.tar.gz
mv data/* ntidata/.
cd ntidata
mysql --local-infile=1 -h localhost -u root -p
source drop.sql
source drop_index.sql
source load_data.sql
source load_index.sql
source library/digital_library.sql

```

### Loading data
```
docker exec -it mariadb bash
mysql --local-infile=1 -h localhost -u root -p

# In the mysql client
# Edit password in the script
source cndata/dictionary.ddl
source cndata/load_data.sql
```

## Web Front End
The web front end for the NTI Reader uses the Chinese Notes Go application,
with source code at

https://github.com/alexamies/chinesenotes.com/tree/master/go/src/cnweb

The instructions for building a Docker image are at
[Chinese Notes](https://github.com/alexamies/chinesenotes.com) 

After following those instructions, execute the Kubernetes commands here:
```
kubectl apply -f kubernetes/app-deployment.yaml 
kubectl apply -f kubernetes/app-service.yaml
```

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
    --path-rules="/find/*=ntireader-service,/findmedia/*=ntireader-service" \
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
