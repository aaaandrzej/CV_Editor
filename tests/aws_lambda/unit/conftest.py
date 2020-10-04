"""Shared fixtures"""

import pytest


@pytest.fixture
def db_credentials(monkeypatch):
    monkeypatch.setenv('DB_HOST', 'some_host')
    monkeypatch.setenv('DB_PORT', '3306')
    monkeypatch.setenv('DB_PASSWORD', 'testing')
    monkeypatch.setenv('DB_USER', 'testing')
    monkeypatch.setenv('DB_NAME', 'testing')


@pytest.fixture
def aws_credentials(monkeypatch):
    """Mocked AWS Credentials for moto."""
    monkeypatch.setenv('AWS_ACCESS_KEY_ID', 'testing')
    monkeypatch.setenv('AWS_SECRET_ACCESS_KEY', 'testing')
    monkeypatch.setenv('AWS_SECURITY_TOKEN', 'testing')
    monkeypatch.setenv('AWS_SESSION_TOKEN', 'testing')
