

clear

SERVER_ALIAS="DEVELOPMENT"
SERVER_ADDRESS="54.191.0.133"


if [ "$1" = "prod" ] || [ "$1" =  "--prod" ] || [ "$1" =  "--producao" ] || [ "$1" = "producao" ]; then
	SERVER_ALIAS="PRODUCTION"
	SERVER_ADDRESS="54.213.143.121"
fi

echo "[Migrating code]"
echo "... server alias: $SERVER_ALIAS"
echo "... server ip: $SERVER_ADDRESS"
echo

echo "... connecting to the host machine"
ssh -i "../WannaMigrate.pem" ubuntu@$SERVER_ADDRESS -t '
GIT_REPO="https://github.com/humbertomn/wannamigrate.git"
DEPLOYMENT_PATH="/wanna"
echo "... checking if git is installed"
hash git &> /dev/null
if [ $? -eq 1 ]; then
    echo "... git not found. Installing"
    sudo apt-get install git
fi
echo "... checking directory"
if [ -d "/wanna" ]; then
    echo "... $DEPLOYMENT_PATH already exists, pulling modifications"
    cd $DEPLOYMENT_PATH
    git pull
else
    echo "... cloning repository $GIT_REPO into $DEPLOYMENT_PATH"
    sudo mkdir /wanna
    sudo chown ubuntu:ubuntu /wanna
    git clone $GIT_REPO $DEPLOYMENT_PATH
    echo "... running configuration script"
    sudo bash /wanna/__infra/scripts/configure.sh
fi'