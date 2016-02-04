# -*- coding:utf-8 -*-

import requests


def test_get_todos():
    r = requests.get('http://localhost:5000/test').json()
    assert r == {'test': 'something'}


def test_put_todos():
    r = requests.put('http://localhost:5000/todo1',
                     data={
                         'data': 'todo1'
                     }).json()
    assert r == {'todo1': 'todo1'}
