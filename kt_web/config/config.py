# -*- coding:utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass
