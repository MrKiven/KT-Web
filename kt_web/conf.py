# -*- coding:utf-8 -*-

from consts import (
    DEV_CONFIG,
    TEST_CONFIG,
    PRODUCTION_CONFIG
)


class Config(object):
    pass

settings = Config()
setattr(settings, 'dev', DEV_CONFIG)
setattr(settings, 'test', TEST_CONFIG)
setattr(settings, 'prod', PRODUCTION_CONFIG)
