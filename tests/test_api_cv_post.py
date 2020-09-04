from unittest.mock import patch
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


# @patch('app.main.User')
# @patch('app.main.replace_skills_with_json')
# @patch('app.main.replace_experience_with_json')
def test_api_cv_post_valid_json(app, api_cv_post):
    with app.test_client() as c:
        rv = c.post('/api/cv', json={'a_key': 'a value'})
        json_data = request.get_json()
        # actual = api_cv_post()

        assert json_data == {'a_key': 'a value'}



@pytest.mark.skip('WIP')
@patch('app.main.get_session')
@patch('app.main.request')
@patch('app.main.User')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_exception_when_no_json(replace_experience_with_json_mock, replace_skills_with_json_mock,
                                request_mock, user_mock, get_session_mock, api_cv_post, app):
    with app.test_client() as c:
        rv = c.post('/api/cv', json={'firstname': 'sdfsf', 'lastname': 'dsds'})
        json_data = rv.get_json()
        # request_mock.get_json.return_value = {'firstname': 'sdfsf', 'lastname': 'dsds'}
        actual = api_cv_post()
        expected = ({'success': 'item added'}, 201)
        assert actual == expected


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
