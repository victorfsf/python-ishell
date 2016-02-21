# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Django
from tests.utils import set_up
from tests.utils import tear_down
import django
import IPython

mock_options_create = {
    'profile': 'test',
    'active': True
}

mock_options = {
    'profile': 'test',
}

mock_options_1 = {
    'profile': 'test',
    'settings': 'test.settings'
}


def mock(monkeypatch):

    def mock_return_none(*args, **kwargs):
        return

    monkeypatch.setattr(IPython, 'start_ipython', mock_return_none)
    monkeypatch.setattr(django, 'setup', mock_return_none)


def mock_raises(monkeypatch):

    def mock_return_none(*args, **kwargs):
        return

    def mock_setup_error(*args, **kwargs):
        raise Exception

    monkeypatch.setattr(IPython, 'start_ipython', mock_return_none)
    monkeypatch.setattr(django, 'setup', mock_setup_error)


def test_django(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Django.run(mock_options)
    tear_down()


def test_django_settings(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Django.run(mock_options_1)
    tear_down()


def test_django_invalid_settings(monkeypatch):
    mock_raises(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Django.run(mock_options_1)
    tear_down()