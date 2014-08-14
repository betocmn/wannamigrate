#!/bin/bash
# This script should run with SU privilegies
echo "--------------------------"
echo "APT-GET UPDATE AND PYTHON3"
echo "--------------------------"
apt-get update
apt-get install python3-dev --yes
echo "--------------------------------------------"
echo "INSTALLING PIP WITH PYTHON 3"  
echo "--------------------------------------------"
cd ~/
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
echo "--------------------------------------------"
echo "INSTALLING VIRTUALENV WITH PYTHON 3"  
echo "--------------------------------------------"
sudo pip install virtualenv
echo "--------------------------------------------"
echo "INSTALLING GIT"  
echo "--------------------------------------------"
apt-get install git --yes
echo "--------------------------"
echo "INSTALLING APACHE"
echo "--------------------------"
apt-get install apache2 --yes
apt-get install libapache2-mod-wsgi-py3 --yes
echo "--------------------------"
echo "INSTALLING MYSQL TOOLS"
echo "--------------------------"
apt-get install libmysqlclient-dev --yes
apt-get install mysql-client --yes
debconf-set-selections <<< 'mysql-server mysql-server/root_password password wanna#surf.au'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password wanna#surf.au'
apt-get -y install mysql-server
echo "--------------------------"
echo "CREATING THE VIRTUAL ENVIRONMENT"
echo "--------------------------"
virtualenv /wannavenv
source /wannavenv/bin/activate
pip install django
pip install https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-1.1.6.tar.gz
deactivate
echo "--------------------------"
echo "UPDATING APACHE CONFIGURATION FILES"
echo "--------------------------"
cp /infra/config/wsgi.conf /etc/apache2/mods-enabled/wsgi.conf
cp /infra/config/wannamigrate.conf /etc/apache2/sites-enabled/wannamigrate.conf
service apache2 restart