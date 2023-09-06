#!/usr/bin/env bash
# script sets up your web servers for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test

printf %s "<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>
" > /data/web_static/releases/test/index.html

mydir='/data/web_static/current'
if [ -L $mydir ]; then
  rm -R '/data/web_static/current'
fi

chown -R ubuntu /data/
chgrp -R ubuntu /data/

ln -s /data/web_static/releases/test /data/web_static/current

printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /etc/nginx/html;
     index       index.html index.htm;

     location /hbnb_static {
        alias  /data/web_static/current;
     }
}
" > /etc/nginx/sites-available/default
service nginx restart
