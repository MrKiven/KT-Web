# -*- coding:utf-8 -*-

from flask_restful import Resource, reqparse

from exc import NotFoundResourceException

todos = {
    'test': 'something'
}


class ParserMixin(object):
    """参数解析Mixin
    """

    @staticmethod
    def get_key(key, required=False):
        parser = reqparse.RequestParser()
        parser.add_argument(key, type=str, help="", required=required)
        return parser.parse_args().get(key)


class Todo(Resource, ParserMixin):
    def get(self, todo_id):
        todo = todos.get(todo_id, None)
        if todo is None:
            raise NotFoundResourceException('todo `{}` not found'.format(todo_id))
        return todo

    def put(self, todo_id):
        data = self.get_key('data', required=True)
        # todos[todo_id] = request.form['data']
        todos[todo_id] = data
        return {todo_id: todos[todo_id]}


class Todos(Resource):
    def get(self):
        return todos
