#Installation without Docker
This page explains setup of combined build and web app. If you are only
installing one or the other you may skip some steps.

## Prerequisites
1. Debian flavor of Linux
2. About 10 GB of memory for the build server, much less for only the web app
3. GCS bucket [optional for build script to upload artifacts]
4. Attached block storage device

## Basic Setup
```
sudo apt-get update

sudo mkdir -p /disk1/ntireader
-- Mount and format disk
-- Add to file system table
sudo vi /etc/fstab
sudo mount -a
```

## NTI Reader Files
```
-- Substitute for your own location and user name
export CNREADER_HOME=/disk1/ntireader
sudo chown $USER:$USER /disk1/ntireader
sudo apt-get install -y git
git clone git://github.com/alexamies/buddhist-dictionary $CNREADER_HOME
```

## Build generated HTML files
```
# Install Go lang
# Get the cnreader build tool
sudo mkdir -p /disk1/cnreader
sudo chown $USER:$USER /disk1/cnreader
export DEV_HOME=/disk1/cnreader
git clone https://github.com/alexamies/chinesenotes.com.git $DEV_HOME
cd $DEV_HOME/go/src/cnreader
go build cnreader
cd $CNREADER_HOME
bin/build.sh
```

## Upload to a GCS bucket
```
export BUCKET={your bucket}
bin/push.sh

# On the application server
# Apache Setup
sudo apt-get install -y apache2 php5 php5-mysql

# Repeat getting of gitbug repo, only buddhist-dictionary (ntireader) is required
# Pull the generated files from GCS
bin/pull.sh

# If your staging environment is different from your prod environment
bin/deploy.sh
```

Set document root

SetEnv DB_PASSWORD 
```
sudo vi /etc/apache2/sites-enabled/000-default
```

Copy Angular files
```
wget https://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js
wget https://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular-sanitize.js 
```

Start Apache2 by default (Debian specific)
```
sudo update-rc.d apache2 defaults
```

Start the server
```
export DB_PASSWORD={password}
sudo apacheclt restart
```

## MySQL Setup
```
sudo apt-get install -y mysql-server mysql-client
```

Load data into database, see ../data/dictionary/dictionary-readme.txt
