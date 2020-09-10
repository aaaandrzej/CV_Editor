from unittest.mock import patch
import pytest


@pytest.fixture
def api_cv_post(db_credentials):
    from app.main import api_cv_post
    return api_cv_post


@pytest.fixture
def app(db_credentials):
    from app.main import app
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize('test_input', [{
    "firstname": "Test",
    "lastname": "1",
    "skills": [],
    "experience": []
},
    {
        "firstname": "Second Test",
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
    },
    {
        "firstname": "3rd Test",
        "lastname": "User",
        "dummy_key": "doesn't matter",
        "skills": [],
        "experience": [
            {
                "company": "Firma",
                "project": "Project",
                "duration": 5
            }
        ]
    },
    {
        "firstname": "3rd Test",
        "lastname": "User",
        "dummy_key": "doesn't matter",
        "skills": [],
        "experience": [
            {
                "company": "Firma",
                "project": "Project",
                "duration": 5
            },
            {
                "company": "Firma2",
                "project": "Project",
                "duration": 5
            },
            {
                "company": "Firma3",
                "project": "Project",
                "duration": 5
            }
        ]
    }
])
@patch('app.main.get_session')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_api_post_cv_with_success(replace_experience_with_json_mock, replace_skills_with_json_mock,
                                  get_session_mock, test_input, api_cv_post, client):
    client.post('/api/cv', json=test_input)

    actual = api_cv_post()
    expected = ({'success': 'item added'}, 201)
    assert actual == expected


@pytest.mark.parametrize('test_input', [{
    "lastname": "no firstname",
    "skills": [],
    "experience": []
},
    {
        "firstname": "no skills",
        "lastname": "User",
        "experience": [
            {
                "company": "Firma",
                "project": "Project",
                "duration": 5
            }
        ]
    },
    {
        "firstname": "no exp",
        "lastname": "User",
        "dummy_key": "doesn't matter",
        "skills": []
    },
    {}
])
@patch('app.main.get_session')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_api_post_cv_with_error(replace_experience_with_json_mock, replace_skills_with_json_mock,
                                get_session_mock, test_input, api_cv_post, client):
    client.post('/api/cv', json=test_input)

    # TODO tak naprawdę to parametrize tu nie ma znaczenia, bo bez tego mocka poniżej funkcja endpointu daje sukces
    # Masz rację, gdyż w tym przypadku to, czy będzie ok, czy nie decyduje payload, tylko to, co rzucą funkcje
    # replace*. Dlatego w tym przypadku parametrize powinien mieć następujące parametry: exception rzucony przez
    # pierwszą funkcję (możesz podać None, jeśli funkcja ma skończyć się poprawnie i wtedy nie wywołasz w teście
    # .side_effect), exception rzucony przez drugą funkcję, oczekiwana odpowiedź. I wszystkie kombinacje :)
    replace_experience_with_json_mock.side_effect = KeyError
    replace_skills_with_json_mock.side_effect = KeyError

    actual = api_cv_post()
    expected = ({'error': 'bad input data'}, 400)
    assert actual == expected


def test_api_cv_post_no_db_error(client, api_cv_post, test_input={
    "firstname": "Test",
    "lastname": "User",
    "skills": [],
    "experience": []
}):
    client.post('/api/cv', json=test_input)
    actual = api_cv_post()
    expected = ({'error': 'db error'}, 500)
    assert actual == expected
