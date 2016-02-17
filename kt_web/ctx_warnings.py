# -*- coding: utf-8 -*-

import contextlib
import warnings
import functools


class CatchWarnMixin(object):
    """Catch Warnings by a contextmanager or a decorator
    Usage:

        @CatchWarnMixin.warning()
        def a_func():
            warnings.warn('some warning')

        or

        with CatchWarnMixin.catchWarnings():
            warnings.warn('some warning')
    """

    @staticmethod
    @contextlib.contextmanager
    def catchWarnings(action='default'):
        warnings.simplefilter(action)
        yield
        warnings.resetwarnings()

    @staticmethod
    def warning(action='default'):
        def so(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                warnings.simplefilter(action)
                try:
                    return func(*args, **kwargs)
                finally:
                    warnings.resetwarnings()
            return wrapper
        return so
