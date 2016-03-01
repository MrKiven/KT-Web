# -*- coding:utf-8 -*-

from blinker import signal

test = signal('test')


class Receiver(object):

    def __init__(self):

        def handle_frobnicated(sender, **kwargs):
            self.on_frobnicated(sender, **kwargs)

        self.handle_frobnicated = handle_frobnicated
        test.connect(handle_frobnicated)

    def on_frobnicated(self, sender, **kwargs):
        print sender, '===', kwargs['message']


if __name__ == '__main__':
    r = Receiver()
    for i in xrange(10):
        test.send('Sender %s' % i, message='hello')
