# -*- coding:utf-8 -*-

from kt_web.api.app import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_todo(client):
    r = client.get('/todos/test')
    # `r` is a Response streamd
    assert r.status_code == 200
    assert r.data.rstrip() == '"something"'
