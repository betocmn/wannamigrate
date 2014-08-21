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
echo "### Instaling Python3 WSGI ###"
apt-get install libapache2-mod-wsgi-py3 --yes
echo "### Instaling PHP and PHP-MYSQL Modules ###"
apt-get install libapache2-mod-php5 --yes
apt-get install php5-mysql --yes
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
echo "DOWNLOADING MEDIA WIKI"
echo "--------------------------"
cd /wanna
wget http://releases.wikimedia.org/mediawiki/1.23/mediawiki-1.23.2.tar.gz
tar -zxf mediawiki-1.23.2.tar.gz
rm mediawiki-1.23.2.tar.gz
mv mediawiki-1.23.2 wiki
echo "--------------------------"
echo "UPDATING APACHE CONFIGURATION FILES"
echo "--------------------------"
cp /wanna/__infra/config/wsgi.conf /etc/apache2/mods-enabled/wsgi.conf
cp /wanna/__infra/config/wannamigrate.conf /etc/apache2/sites-enabled/wannamigrate.conf
rm /etc/apache2/sites-enabled/000-default.conf
service apache2 restart

echo "########################################"
echo "         CONFIGURATION DONE!"
echo "########################################"
echo "You need to do some configurations manually. Follow the next steps:"
echo "1. Connect to the guest machine via SSH."
echo "   => vagrant ssh"
echo "   or"
echo "   => ssh -i ../WannaMigrate.pem ubuntu@SERVER_ADDRESS, where SERVER_ADDRESS is the IP of the server on amazon."
echo "2. Access your mysql and create a database called 'wannamigrate'"
echo "   => mysql -u root -p"
echo "3. Activate your virtualenv and run a 'syncdb' inside your django application."
echo "   => source /wannavenv/bin/activate"
echo "   => python /wanna/app/wannamigrate/manage.py syncdb"
echo "4. If you want to configure your wiki, access http://localhost:8181/mw-config/index.php and follow the installation instructions"
