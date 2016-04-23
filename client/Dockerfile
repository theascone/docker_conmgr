FROM httpd:latest
MAINTAINER Addis Dittebrant <addis.dittebrandt@gmail.com>

RUN apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade
RUN apt-get -y install npm nodejs nodejs-legacy

WORKDIR /usr/local/apache2/htdocs/
COPY ./package.json /usr/local/apache2/htdocs/
RUN npm install

COPY ./ /usr/local/apache2/htdocs/
RUN npm run release

ENV NODE_ENV=production
RUN npm prune

RUN sed -i 's|^#LoadModule proxy_module|LoadModule proxy_module|' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's|^#LoadModule proxy_http_module|LoadModule proxy_http_module|' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's|^#Include conf/extra/httpd-vhosts.conf|Include conf/extra/httpd-vhosts.conf|' /usr/local/apache2/conf/httpd.conf
RUN mv ./apache/httpd-vhosts.conf /usr/local/apache2/conf/extra/ && rmdir apache
