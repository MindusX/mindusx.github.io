# 1. Créez un fichier .env
echo "SECRET_KEY=super-secret
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_FROM_NUMBER=+33123456789" > .env

# 2. Construisez et lancez
docker compose up --build