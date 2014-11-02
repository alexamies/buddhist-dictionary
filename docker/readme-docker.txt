#
# Cheat Sheet for Docker commands for NTI Reader
#

# (0) These instructions assume that Docker is installed and you are running on Linux.

# (1) Install git on the host and checkout the code base
sudo apt-get update
sudo apt-get install -y git
git clone git://github.com/alexamies/buddhist-dictionary $HOME/ntireader
cd ntireader/docker

# Database
sudo docker run --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin -d mysql
sudo docker inspect db | grep IPAddress

# Admin client
sudo docker run -it -v $HOME/ntireader/data/dictionary:/var/dictionary --link db:mysql --name admin_client --rm -w /var/dictionary mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'

# Follow instructions in dictionary-readme.txt to create and load the dictionary database

# Web server
docker build -t="ntireader-www:0.53" ntireader-www/
docker run -d -p 80:80 --name web -v $HOME/ntireader/web:/var/www/html/ ntireader-www:0.53

# Ubuntu utility
docker run --rm -it $HOME/ntireader/:/ntireader --link web:web --link db:db --rm -w="/var/ntireader" ubuntu /bin/bash
