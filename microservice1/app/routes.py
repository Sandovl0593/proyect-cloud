from app.controllers import *
from app import api

# API resource routes
api.add_resource(Index, '/')
api.add_resource(UserList, '/utecshop/usuarios', endpoint='usuarios')
api.add_resource(User, '/utecshop/usuario/<username>', endpoint='usuario')
api.add_resource(Register, '/utecshop/register', endpoint='register')