from app.controllers import *
from app import api

# API resource routes
api.add_resource(Productos, '/utecshop/productos', endpoint='productos')
api.add_resource(Inventario, '/utecshop/inventario', endpoint='inventario')