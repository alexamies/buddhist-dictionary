#
# Docker build file for NTI Reader web server
#

FROM ubuntu:14.04
MAINTAINER Alex <alex@chinesenotes.com>
RUN apt-get update && apt-get install -y apache2 php5 php5-mysql
RUN mkdir /var/ntireader
RUN cp -rf /var/ntireader/web/* /var/www/html/.

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

VOLUME ["/var/log/apache2"]

EXPOSE 80

ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D", "FOREGROUND"]