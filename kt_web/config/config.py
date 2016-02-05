# -*- coding:utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass
