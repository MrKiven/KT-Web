# -*- coding:utf-8 -*-

import logging
import logging.config
import yaml

from app import app

logging.config.dictConfig(yaml.load(open('logging.conf')))
logfile = logging.getLogger('file')
logconsole = logging.getLogger('console')

app.logger.info('Logging is set up')
