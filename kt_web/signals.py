# -*- coding:utf-8 -*-

from blinker import signal


class SignalContext(object):
    pass


class ApiCallSignalContext(SignalContext):

    @property
    def cost(self):
        return '%.2f ms' % (1000 * (self.end_at - self.start_at))


before_api_called = signal('before_api_called')
after_api_called = signal('after_api_called')


def register_signals_receivers():
    before_api_called.connect(on_signal_before_api_called)
    after_api_called.connect(on_signal_after_api_called)


def on_signal_before_api_called(ctx):
    pass


def on_signal_after_api_called(ctx):
    print 'cost --->', ctx.cost
