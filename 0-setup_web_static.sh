#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install nginx
apt-get update
apt-get install -y nginx

# Create directories and symbolic link
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# Add html content to index
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

# Create a symblic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu
chown -R ubuntu:ubuntu /data/

# Update nginx config
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.save
sed -i 's/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}/'\
       	/etc/nginx/sites-available/default

# Restart nginx to apply changes
service nginx restart
