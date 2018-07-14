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
mkdir ntidata
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

Test it locally
First, export environment variables `DBUSER` and `DBPASSWORD` to connect to the 
database, as per unit tests above.

```
docker run -itd --rm -p 80:80 --name ntireader-web --link mariadb \
  -e DBUSER=$DBUSER \
  -e DBPASSWORD=$DBPASSWORD \
  ntireader-web-image
```

Attach to a local image for debugging, if needed
```
docker exec -it ntireader-web bash
```

Push to Google Container Registry
[Google Container Registry Quickstart](https://cloud.google.com/container-registry/docs/quickstart)

```
TAG=prototype01
docker tag ntireader-web-image gcr.io/$PROJECT/ntireader-web-image:$TAG
gcloud docker -- push gcr.io/$PROJECT/ntireader-web-image:$TAG

```
