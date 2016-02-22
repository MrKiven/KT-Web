# -*- coding:utf-8 -*-


class KTWEBException(Exception):
    """API Exception Handler Class"""
    status_code = 500

    def __init__(self, msg, status_code=None, payload=None):
        super(KTWEBException, self).__init__()
        self.msg = msg
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.msg
        rv['status_code'] = self.status_code
        return rv


class NotFoundResourceException(KTWEBException):

    def __init__(self, msg, status_code=404, payload=None):
        super(NotFoundResourceException, self).__init__(msg, status_code, payload)
