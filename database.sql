DROP DATABASE IF EXISTS proyecto;
CREATE DATABASE proyecto CHARSET utf8mb4;
USE proyecto;

CREATE TABLE IF NOT EXISTS usuario (
    username VARCHAR(80) PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL, 
    phone VARCHAR(9) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL, 
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS producto (
    codigo_p VARCHAR(6) PRIMARY KEY NOT NULL, 
    usuario_p VARCHAR(80) NOT NULL, 
    nombre VARCHAR(40) NOT NULL, 
    precio FLOAT NOT NULL, 
    marca VARCHAR(30) NOT NULL, 
    categoria VARCHAR(30) NOT NULL 
);

CREATE TABLE IF NOT EXISTS compra (
    codigo_c VARCHAR(6) PRIMARY KEY NOT NULL, 
    codigo_p VARCHAR(6) NOT NULL, 
    usuario_c VARCHAR(80) NOT NULL, 
    usuario_v VARCHAR(80) NOT NULL
);