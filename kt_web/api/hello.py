# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_restful import Api, Resource

bp = Blueprint('hello', __name__)
api = Api(bp)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')
