"""Shared fixtures"""

import pytest

# from app.main import *


@pytest.fixture
def mock_json_data_correct():
    return {
        "firstname": "Test",
        "lastname": "User",
        "skills": [
            {
                "skill_name": "skill1",
                "skill_level": 1
            },
            {
                "skill_name": "skill2",
                "skill_level": 2
            }
        ],
        "experience": [
            {
                "company": "Firma",
                "project": "Project",
                "duration": 5
            }
        ]
    }


@pytest.fixture
def mock_json_data_no_exp():
    return {
        "abc": "def"
    }


@pytest.fixture
def mock_json_data_incorrect_exp():
    return {
        "experience": [
            {
                "wrong_key": "Firma"
            }
        ]
    }


@pytest.fixture
def db_credentials(monkeypatch):
    monkeypatch.setenv('DB_HOST', 'some_host')
    monkeypatch.setenv('DB_PORT', 3306)
    monkeypatch.setenv('DB_ROOT_PASSWORD', 'testing')
    monkeypatch.setenv('DB_ROOT_USER', 'testing')
    monkeypatch.setenv('DB_USER', 'testing')
    monkeypatch.setenv('DB_PASSWORD', 'testing')
    monkeypatch.setenv('DB_NAME', 'testing')
