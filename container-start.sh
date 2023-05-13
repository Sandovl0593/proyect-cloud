#!/bin/bash

directorio=$(pwd)

if [ "$directorio" != "/home/ubuntu/proyect-cloud" ]; then
    cd home/ubuntu/proyect-cloud
fi

host=$1

sed -i "1s/.*VITE_API_HOST=${host}" "./frontend/src/views/.env"

docker-compose up -d