# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from hello import HelloWorld
from todos import Todo, Todos

ktweb_bp = Blueprint('KT_WEB_API', __name__)

api = Api(ktweb_bp)

api.add_resource(HelloWorld, '/hello')
api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')
