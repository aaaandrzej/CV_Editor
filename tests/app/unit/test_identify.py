import pytest
from unittest.mock import patch

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
def test_identify_endpoint(extract_user_mock, client):

    extract_user_mock.return_value = User(username='test', password='test', firstname='te', lastname='st', admin=True)

    response = client.get('/identify')
    actual = response.get_json(), response.status_code

    assert actual == ({'admin': True, 'experience': [], 'firstname': 'te', 'id': None, 'lastname': 'st', 'skills': [], 'username': 'test'}, 200)
