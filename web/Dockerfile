FROM node:latest

WORKDIR /frontend/app

# Ejecuta solo por primera y unica vez
COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]