# -*- coding:utf-8 -*-

import time

from flask import Flask, request, jsonify

from api.exc import NotFoundResourceException
# Resources
from api import ktweb_bp
from models import init_db

from settings import current_env
from signals import (
    ApiCallSignalContext,
    register_signals_receivers,
    before_api_called,
    after_api_called
)


class KTWEB(Flask):

    def __init__(self):
        super(KTWEB, self).__init__('KTWEB')
        self.url_prefix = '/api'
        self.ctx = ApiCallSignalContext()
        self.register_signals()
        self.config.from_object(current_env)
        self.register_blueprints()
        self.register_error_handlers()
        self.register_before_request_funcs()
        self.register_after_request_funcs()

    def register_signals(self):
        register_signals_receivers()

    def register_blueprints(self):
        self.register_blueprint(ktweb_bp, url_prefix=self.url_prefix)

    def register_error_handlers(self):
        self.register_error_handler(NotFoundResourceException, self.not_found)

    def register_before_request_funcs(self):
        self.before_request(self.record_request_start_at)

    def register_after_request_funcs(self):
        self.after_request(self.send_request_metrics)

    def record_request_start_at(self):
        request.start_at = time.time()
        self.ctx.start_at = request.start_at
        before_api_called.send(self.ctx)

    def send_request_metrics(self, resp):
        def send_metrics():
            if not request.endpoint:
                return
            request.end_at = time.time()
            self.ctx.end_at = request.end_at
            after_api_called.send(self.ctx)
        send_metrics()
        return resp

    @staticmethod
    def not_found(err):
        res = jsonify(err.to_dict())
        res.status_code = err.status_code
        return res

app = KTWEB()
init_db(app)
