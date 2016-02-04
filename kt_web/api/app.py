# -*- coding:utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Api

from exc import NotFoundResourceException
# Resources
from todos import Todo, Todos
from hello import HelloWorld

app = Flask(__name__)
api = Api(app)


@app.errorhandler(NotFoundResourceException)
def handler_error(err):
    res = jsonify(err.to_dict())
    res.status_code = err.status_code
    return res


api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(Todos, '/todos/')
api.add_resource(HelloWorld, '/hello')
