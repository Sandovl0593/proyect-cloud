from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flaskext.mysql import MySQL

# Create instance of Flask app
app = Flask(__name__)
CORS(app)

#Create an instance of MySQL and Flask RESTful API
db = MySQL()
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'proyecto'
app.config['MYSQL_DATABASE_HOST'] = ''
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
db.init_app(app)

from app import controllers
from app import routes