#
# Cheat Sheet for Docker commands for NTI Reader
#

# (0) These instructions assume that Docker is installed and you are running on Linux.

# (1) Install git on the host and checkout the code base
sudo apt-get update
sudo apt-get install -y git
git clone git://github.com/alexamies/buddhist-dictionary $HOME/ntireader
cd ntireader/docker

# (2) Database
sudo docker run --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin -d mysql
sudo docker inspect db | grep IPAddress

# (3) Admin client
sudo docker run -it -v $HOME/ntireader/data/dictionary:/var/dictionary --link db:mysql --name admin_client --rm -w /var/dictionary mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'

# Follow instructions in dictionary-readme.txt to create and load the dictionary database

# (4) Web server
vi web/inc/database_utils.php
# Edit to refer to db address with passwd
sudo docker build -t="ntireader-www:0.53" ntireader-www/
sudo docker run -d -p 80:80 --name web --link db:db -v $HOME/ntireader/web:/var/www/html/ ntireader-www:0.53
sudo docker inspect web | grep IPAddress
curl <IPAddress>

# Troubleshooting: Ubuntu utility with connections into the web and mysql containers
sudo docker run --rm -it --link web:web --link db:db --rm --volumes-from=web ubuntu /bin/bash

# (5) Use the command line tool to generate corpus files
# The HTML gloss and vocabulary analysis markdown files are generated from the text files in the GitHub project
sudo apt-get install -y python-bs4
sudo apt-get install python-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install regex
# Run command line utilities from host to populate corpus gloss and analysis files
cd command-line
python bdictutil.py --help