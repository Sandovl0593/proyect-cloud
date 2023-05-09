from app.controllers import *
from app import api

# API resource routes
api.add_resource(Index, '/')
api.add_resource(UserList, '/utecshop/users', endpoint='users')
api.add_resource(User, '/utecshop/user/<username>', endpoint='user')
api.add_resource(Register, '/utecshop/register', endpoint='register')