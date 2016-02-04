# -*- coding:utf-8 -*-

from flask import request
from flask_restful import Resource

from exc import NotFoundResourceException

todos = {
    'test': 'something'
}


class Todo(Resource):
    def get(self, todo_id):
        todo = todos.get(todo_id, None)
        if todo is None:
            raise NotFoundResourceException('todo `{}` not found'.format(todo_id))
        return todo

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


class Todos(Resource):
    def get(self):
        return todos
