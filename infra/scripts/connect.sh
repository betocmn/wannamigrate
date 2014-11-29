clear

SERVER_ALIAS="DEVELOPMENT"
SERVER_ADDRESS="54.191.0.133"


if [ "$1" = "prod" ] || [ "$1" =  "--prod" ] || [ "$1" =  "--producao" ] || [ "$1" = "producao" ]; then
    SERVER_ALIAS="PRODUCTION"
    SERVER_ADDRESS="54.148.167.28"
fi

echo "[Connecting to server]"
echo "... server alias: $SERVER_ALIAS"
echo "... server ip: $SERVER_ADDRESS"
echo

echo "... connecting to the host machine"
ssh -i "../WannaMigrate.pem" ubuntu@$SERVER_ADDRESS