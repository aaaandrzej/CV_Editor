from unittest.mock import patch, MagicMock
from flask import request, session
import pytest
from app.models import User, SkillUser, SkillName, Experience


@pytest.fixture
def api_cv_post(db_credentials):
    from app.main import api_cv_post
    return api_cv_post


@pytest.fixture
def app(db_credentials):
    from app.main import app
    return app


# @pytest.fixture
# def client(app):
#     with app.test_client() as client:
#         return client


def test_api_cv_post_no_db_error(app):
    rv = app.test_client().post('/api/cv/', data='random data')
    assert rv.data == b'{"error":"bad input data"}\n'


def test_api_cv_post_request_get_json(app, api_cv_post):  # tutaj udało się dobić do request.get_json()
    with app.test_client() as c:
        rv = c.post('/api/cv', json={'a_key': 'a value'})
        json_data = request.get_json()
        assert json_data == {'a_key': 'a value'}


@patch('app.main.get_session')
# @patch('app.main.User')
# @patch('app.main.replace_skills_with_json')
# @patch('app.main.replace_experience_with_json')
def test_api_post_cv_with_success(get_session_mock, api_cv_post, app):  # to teraz przechodzi, aż sam jestem w szoku
    with app.test_client() as c:
        rv = c.post('/api/cv', json={
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
        })

        get_session_mock.return_value = MagicMock()

        actual = api_cv_post()
        expected = ({'success': 'item added'}, 201)
        assert actual == expected


@pytest.mark.skip('WIP')
def test_exception_when_no_json(api_cv_post, app):
    pass


@pytest.mark.skip('WIP')
def test_exception_when_no_key():
    with pytest.raises(KeyError):
        new_cv = User()
        json_data = {'a': 1}
        new_cv.firstname = json_data['firstname']
        pass


@pytest.mark.skip('WIP')
def test_exception_when_wrong_json():
    # raises AttributeError?
    pass


@pytest.mark.skip('WIP')
def test_exception_when_TypeError___():
    # hmm
    pass


@pytest.mark.skip('WIP')
def test_exception_when_db_error():
    # raises DataError
    pass


@pytest.mark.skip('WIP')
def test_cv_added_on_success():
    # assert {'success': 'item added'}, 201
    pass
