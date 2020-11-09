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


def test_index_response(client):

    rv = client.get('/')
    assert rv.data == b'For API please use /api/cv or /api/cv/<id>'
