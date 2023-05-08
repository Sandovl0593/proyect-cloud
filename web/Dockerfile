FROM node:latest

WORKDIR /web/app

# Ejecuta solo por primera y unica vez
COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]