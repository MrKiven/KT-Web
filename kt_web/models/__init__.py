# -*- coding:utf-8 -*-

import logging
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)
db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ktweb.db'
    db.init_app(app)
    db.app = app
    db.create_all()
    return db
