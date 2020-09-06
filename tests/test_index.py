import pytest


@pytest.fixture
def app(db_credentials):
    from app.main import app
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        return client


def test_index_response(client):
    rv = client.get('/')
    assert rv.data == b'For API please use /api/cv or /api/cv/<id>'
