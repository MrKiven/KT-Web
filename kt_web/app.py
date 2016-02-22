# -*- coding:utf-8 -*-

import time

from flask import Flask, request, jsonify

from api.exc import NotFoundResourceException
# Resources
from api.todos import bp as todo_bp
from api.hello import bp as hello_bp


class KTWEB(Flask):

    def __init__(self):
        super(KTWEB, self).__init__('KTWEB')
        self.url_prefix = '/api'
        self.config.from_object('kt_web.config.config.DevConfig')
        self.register_blueprints()
        self.register_error_handlers()
        self.register_before_request_funcs()

    def register_blueprints(self):
        self.register_blueprint(hello_bp, url_prefix=self.url_prefix)
        self.register_blueprint(todo_bp, url_prefix=self.url_prefix)

    def register_error_handlers(self):
        self.register_error_handler(NotFoundResourceException, self.not_found)

    def register_before_request_funcs(self):
        self.before_request(self.record_request_start_at)

    def register_after_request_funcs(self):
        pass

    @staticmethod
    def record_request_start_at():
        request.start_at = time.time()

    @staticmethod
    def not_found(err):
        res = jsonify(err.to_dict())
        res.status_code = err.status_code
        return res

app = KTWEB()
