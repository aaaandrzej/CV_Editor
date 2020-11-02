import pytest
from unittest.mock import patch
import undecorated

from app.models import User


@pytest.fixture
def app(db_credentials):
    from app.main import app
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@patch('app.auth.extract_user')
def test_index_response(extract_user_mock, client):

    extract_user_mock.return_value = User(username='test', password='test', firstname='te', lastname='st', admin=True)

    rv = client.get('/')
    assert rv.data == b'Hello test (te st), this is protected'
