from flask import Flask

app = Flask(__name__)

property = {
    "host": "<url>",     #url publica de la MV de la maquina de BD RDS
    "port": 3306  ,      # Puerto de la MV de la maquina de BD RDS
    "user": "root" ,      # your username
    "password": "utec",    # your password
    "database": "default"  # your database
}

from app import routes