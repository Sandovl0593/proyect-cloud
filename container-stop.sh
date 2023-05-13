#!/bin/bash

imagenes=("frontend" "api-usuarios" "api-compra-venta" "api-productos")

for imagen in "${imagenes[@]}"
do
  # Verifica si la imagen existe en el sistema
  if docker images --format '{{.Repository}}:{{.Tag}}' | grep -q "$imagen"; then
    imagen_id=$(docker inspect -f '{{.Image}}' $imagen 2>/dev/null)
    docker stop $imagen_id
done