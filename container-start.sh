#!/bin/bash

directorio=$(pwd)

if [ "$directorio" != "/home/ubuntu/proyect-cloud" ]; then
    cd home/ubuntu/proyect-cloud
fi

docker-compose up -d