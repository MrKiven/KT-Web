# -*- coding:utf-8 -*-


class CachedProperty(object):
    """Decorator like python built-in ``property``, but it results only
    once call, set the result into decorated instance's ``__dict__`` as
    a static property.
    """
    def __init__(self, fn):
        self.fn = fn
        self.__doc__ = fn.__doc__

    def __get__(self, inst, cls):
        if inst is None:
            return
        val = inst.__dict__[self.fn.__name__] = self.fn(inst)
        return val
