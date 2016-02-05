# -*- coding:utf-8 -*-

from flask import Flask, json, jsonify, make_response
from flask_restful import Api

from exc import NotFoundResourceException
# Resources
from todos import Todo, Todos
from hello import HelloWorld

app = Flask(__name__)
api = Api(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    res = make_response(json.dumps(data), code)
    res.headers.extend(headers or {})
    return res


@app.errorhandler(NotFoundResourceException)
def handler_error(err):
    res = jsonify(err.to_dict())
    res.status_code = err.status_code
    return res


api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(Todos, '/todos')
api.add_resource(HelloWorld, '/hello')
