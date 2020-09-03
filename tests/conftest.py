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
