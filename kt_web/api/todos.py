# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from exc import NotFoundResourceException

app = Flask(__name__)
api = Api(app)

todos = {
    'test': 'something'
}


@app.errorhandler(NotFoundResourceException)
def handler_error(err):
    res = jsonify(err.to_dict())
    res.status_code = err.status_code
    return res


class TodoSimple(Resource):
    def get(self, todo_id):
        todo = todos.get(todo_id, None)
        if todo is None:
            raise NotFoundResourceException('`{}` not found'.format(todo_id))
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
