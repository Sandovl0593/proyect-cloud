from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flaskext.mysql import MySQL

# Create instance of Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app, resources={r"/utecshop/*": {"origins": "*"}})

#Create an instance of MySQL and Flask RESTful API
db = MySQL()
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'bd_api'
app.config['MYSQL_DATABASE_HOST'] = '3.231.7.144'
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
db.init_app(app)

from app import controllers, routes