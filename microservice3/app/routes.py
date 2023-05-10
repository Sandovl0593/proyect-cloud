from app.controllers import *
from app import api

# API resource routes
api.add_resource(Vender, '/utecshop/vender', endpoint='vender')
api.add_resource(Inventario, '/utecshop/inventario', endpoint='inventario')