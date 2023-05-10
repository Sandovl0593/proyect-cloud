from controllers import *
from app import api
from app.controllers import *
from app import api

# API resource routes
api.add_resource(RegistrarProducto, '/utecshop/registar_producto', endpoint='registrar_producto')
api.add_resource(Comprar, '/utecshop/comprar', endpoint='comprar')
api.add_resource(RegistrarCompr, '/utecshop/register', endpoint='register')