from myapi import app
import pytest
import os
import tempfile


# http://flask.pocoo.org/docs/1.0/testing/
@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


def test_foo_handler(client):
    """test controller.foo_handler"""
    R = client.get('/foo/aaa')
    assert R.data == b"aaa"
    assert R.status_code == 200


def test_baz_handler(client, monkeypatch):
    """tests controller.foo handler"""
    fake_json = {"query_string": "amazingquery"}
    R = client.post("baz", json=fake_json)
    assert R.data == b"amazingquery"
    assert R.status_code == 200
