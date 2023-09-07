#!/usr/bin/env bash
# script sets up your web servers for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/shared
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

ln -s /data/web_static/releases/test/ /data/web_static/current

printf %s "server {
    listen      80 default_server;
    listen      [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }

    location /hbnb_static {
      alias /data/web_static/current;
      index index.html index.htm;
    }
}
" > /etc/nginx/sites-available/default
service nginx restart
