# -*- coding:utf-8 -*-

from . import db
from kt_web.api.exc import NotFoundResourceException


class TodosModel(db.Model):

    __tablename__ = 'Todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo_name = db.Column(db.String, nullable=False)
    todo_text = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'todo_name': self.todo_name,
            'todo_text': self.todo_text
        }

    @classmethod
    def get(cls, todo_name):
        res = db.session.query(cls).\
            filter(cls.todo_name == todo_name).first()
        if res:
            return res.to_dict()
        raise NotFoundResourceException(
            'todo `{}` not found'.format(todo_name))

    @classmethod
    def all(cls):
        res = db.session.query(cls).all()
        return [r.to_dict() for r in res]
