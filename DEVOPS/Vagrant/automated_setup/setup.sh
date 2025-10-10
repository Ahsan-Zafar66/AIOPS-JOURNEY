#!/bin/bash
echo "!!!!!!!!!!!!!!!!!!!!Updating system!!!!!!"
apt-get update -y
apt-get install apache2 -y


echo "!!!!!!!!!!!Installing Apache2 Service !!!!!!!!!!!"
rm -rf /var/www/html/html.index
service apache2 status
service apache2 restart


echo "Installing php"
apt-get install php5 php5-mysql -y
service apache2 status
service apache2 restart

