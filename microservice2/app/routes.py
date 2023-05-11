from app.controllers import *
from app import api

# API resource routes
api.add_resource(RegistrarProducto, '/utecshop/registrar_producto', endpoint='registrar_producto')
api.add_resource(Tienda, '/utecshop/tienda', endpoint='tienda')
api.add_resource(RegistrarCompra, '/utecshop/registrar_compra', endpoint='registrar_compra')