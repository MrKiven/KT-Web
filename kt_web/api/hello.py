# -*- coding:utf-8 -*-

from flask import jsonify
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world'})
