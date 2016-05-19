# -*- coding:utf-8 -*-

import logging

from app import app

# import logging.config
# import yaml

# logging.config.dictConfig(yaml.load(open('logging.conf')))
# logfile = logging.getLogger('file')
# logconsole = logging.getLogger('console')
logger = logging.getLogger(__name__)
logger.info('Logging is set up')

version_info = (0, 0, 1)
__version__ = ".".join([str(v) for v in version_info])

__all__ = ['app']
