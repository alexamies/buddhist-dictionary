#
# Cheat Sheet for Docker commands for NTI Reader
#

# Database
docker run --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin -d mysql
docker inspect db | grep IPAddress

# Web server
docker build -t="ntireader-www:0.53" ntireader-www/
docker run -d -p 8080:80 --name web ntireader-www:0.53

# Admin client
docker run -it  --volumes-from web -w="/var/ntireader/data/dictionary" --link db:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
docker run --rm -it --volumes-from web --link db:db --rm -w="/var/ntireader/data/dictionary" mysql sh -c 'exec mysql -h172.17.0.91 -P3306 -uroot -padmin'

# Ubuntu utility
docker run --rm -it --volumes-from web --link db:db --rm -w="/var/ntireader" ubuntu /bin/bash
