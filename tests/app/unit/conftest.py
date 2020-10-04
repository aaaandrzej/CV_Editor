"""Shared fixtures"""

import pytest


@pytest.fixture
def db_credentials(monkeypatch):
    monkeypatch.setenv('DB_HOST', 'some_host')
    monkeypatch.setenv('DB_PORT', '3306')
    monkeypatch.setenv('DB_PASSWORD', 'testing')
    monkeypatch.setenv('DB_USER', 'testing')
    monkeypatch.setenv('DB_NAME', 'testing')
