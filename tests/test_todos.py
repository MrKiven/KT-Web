# -*- coding:utf-8 -*-

from kt_web.api.app import app
import pytest


@pytest.fixture
def client():
    client = app.test_client()
    client.testing = True
    return client


def test_todo(client):
    r = client.get('/todos/test')
    # `r` is a Response streamd
    assert r.status_code == 200
    assert r.data.rstrip() == '"something"'


def test_hello(client):
    r = client.get('/hello')
    assert r.status_code == 200
