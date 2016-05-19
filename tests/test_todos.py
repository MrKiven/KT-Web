# -*- coding:utf-8 -*-

import mock
import pytest
import json

from kt_web.app import app
from kt_web.models.record import TodosModel
from kt_web.consts import NOT_FOUND_RESOURCE_MESSAGE


@pytest.fixture
def client():
    client = app.test_client()
    client.testing = True
    return client


def ret(data):
    return json.loads(data)


def test_todo(client):
    with mock.patch.object(TodosModel, 'get', return_value='test'):
        r = client.get('/api/todos/Test')
    # `r` is a Response streamd
    assert r.status_code == 200
    assert ret(r.data) == "test"

    # not found resource
    api = u'invalid_todo_name'
    r = client.get('/api/todos/{}'.format(api))
    assert r.status_code == 404
    _json_ret = ret(r.data)
    assert _json_ret.get('message') == NOT_FOUND_RESOURCE_MESSAGE.\
        format(TodosModel.__name__, api)


def test_hello(client):
    r = client.get('/api/hello')
    assert r.status_code == 200
