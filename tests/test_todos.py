# -*- coding:utf-8 -*-

from kt_web.app import app
import pytest


@pytest.fixture
def client():
    client = app.test_client()
    client.testing = True
    return client


def test_todo(client):
    r = client.get('/api/todos/test')
    # `r` is a Response streamd
    assert r.status_code == 200
    assert r.data.rstrip() == '"something"'


def test_hello(client):
    r = client.get('/api/hello')
    assert r.status_code == 200
