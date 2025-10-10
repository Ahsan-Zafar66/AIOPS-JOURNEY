#!/bin/bash
apt-get install zip
apt-get install vim
apt-get remove -y zip

echo "My name is ahsan and i am runing a script" > /home/vagrant/result.txt
free -g > /home/vagrant/memory_details.txt
