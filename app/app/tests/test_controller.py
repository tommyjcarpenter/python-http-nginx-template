from myapi import controller


# pytest doesnt support objects in conftest yet
class FakeConnexion(object):
    def __init__(self, json):
        self.json = json


def test_foo_handler():
    """test controller.foo_handler"""
    R = controller.foo_handler("aaa")
    assert R.data == b"aaa"
    assert R.status_code == 200


def test_baz_handler(monkeypatch):
    """tests controller.foo handler"""
    fake_json = {"query_string": "amazingquery"}
    monkeypatch.setattr('connexion.request', FakeConnexion(fake_json))

    R = controller.baz_handler()
    assert R.data == b"amazingquery"
    assert R.status_code == 200
