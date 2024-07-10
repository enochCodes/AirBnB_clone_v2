#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install nginx
if dpkg -l | grep nginx
then
	echo "Nginx is already installed."
else
	echo "Installing nginx..."
	sudo apt-get update
	sudo apt-get install nginx
fi

# Create directories and symbolic link
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<h1>AirBnb Clone</h1>" > /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ]
then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/current /data/web_static/releases/test/

# Give ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update nginx config
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.save
sudo sed 's/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/'\
       	/etc/nginx/sites-available/default
