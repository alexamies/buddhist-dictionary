#Installation without Docker

## Basic Setup
sudo apt-get update

sudo mkdir /disk1
-- Mount and format disk
-- Add to file system table
sudo vi /etc/fstab
sudo mount -a

## NTI Reader Files
-- Substitute for your own location and user name
export NTI_HOME=/disk1
sudo /disk1/ntireader
sudo chown alex:alex /disk1/ntireader
sudo apt-get install -y git
git clone git://github.com/alexamies/buddhist-dictionary $NTI_HOME/ntireader

## Apache Setup
sudo -su
apt-get update && apt-get install -y apache2 php5 php5-mysql
exit

-- Set document root
-- SetEnv DB_PASSWORD 
sudo vi /etc/apache2/sites-enabled/000-default

-- Copy Angular files
wget https://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js
wget https://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular-sanitize.js 

-- Start Apache2 by default (Debian specific)
sudo update-rc.d apache2 defaults

-- Start the server
export DB_PASSWORD={password}
sudo apacheclt restart

## MySQL Setup
sudo apt-get install -y mysql-server mysql-client
-- Load data into database, see ../data/dictionary/dictionary-readme.txt
