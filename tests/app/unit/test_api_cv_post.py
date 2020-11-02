from unittest.mock import patch
import pytest
from sqlalchemy.exc import OperationalError, DataError

from app.exceptions import InvalidTokenError, ExpiredTokenError, MissingTokenError
from app.models import User


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


@pytest.mark.parametrize('test_input, replace_skills_with_json_error, replace_experience_with_json_error, expected', [
    (
            {
                'username': 'test',
                'firstname': 'Test',
                'lastname': '1',
                'skills': [],
                'experience': []
            },
            None,
            None,
            ({'admin': False,
              'experience': [],
              'firstname': 'Test',
              'id': None,
              'lastname': '1',
              'skills': [],
              'username': 'test'},
             201)
    ),
    (
            {
                'username': 'second_test',
                'firstname': 'Second Test',
                'lastname': 'User',
                'skills': [
                    {
                        'skill_name': 'skill1',
                        'skill_level': 1
                    },
                    {
                        'skill_name': 'skill2',
                        'skill_level': 2
                    }],
                'experience': [
                    {
                        'company': 'Firma',
                        'project': 'Project',
                        'duration': 5
                    }]
            },
            None,
            None,
            ({'admin': False,
              'experience': [],
              'firstname': 'Second Test',
              'id': None,
              'lastname': 'User',
              'skills': [],
              'username': 'second_test'},
             201)
    ),
    (
            {
                'username': 'test3',
                'firstname': '3rd Test',
                'lastname': 'User',
                'dummy_key': 'doesnt matter',
                'skills': [],
                'experience': [
                    {
                        'company': 'Firma',
                        'project': 'Project',
                        'duration': 5
                    }]
            },
            None,
            None,
            ({'admin': False,
              'experience': [],
              'firstname': '3rd Test',
              'id': None,
              'lastname': 'User',
              'skills': [],
              'username': 'test3'},
             201)
    ),
    (
            {
                'username': '4th_test',
                'firstname': '4th Test',
                'lastname': 'User',
                'dummy_key': 'doesnt matter',
                'skills': [],
                'experience': [
                    {
                        'company': 'Firma',
                        'project': 'Project',
                        'duration': 5
                    },
                    {
                        'company': 'Firma2',
                        'project': 'Project',
                        'duration': 5
                    },
                    {
                        'company': 'Firma3',
                        'project': 'Project',
                        'duration': 5
                    }]
            },
            None,
            None,
            ({'admin': False,
              'experience': [],
              'firstname': '4th Test',
              'id': None,
              'lastname': 'User',
              'skills': [],
              'username': '4th_test'},
             201)
    ),
    (
            {
                'username': 'no_exp',
                'firstname': 'no exp',
                'lastname': 'User',
                'dummy_key': 'doesnt matter',
                'skills': []
            },
            None,
            None,
            ({'admin': False,
              'experience': [],
              'firstname': 'no exp',
              'id': None,
              'lastname': 'User',
              'skills': [],
              'username': 'no_exp'},
             201)
    ),
    (
            {
                'lastname': 'no firstname',
                'skills': [],
                'experience': []
            },
            KeyError,
            KeyError,
            ({'error': 'bad input data'}, 400)
    ),
    (
            {
                'firstname': 'no',
                'lastname': 'no',
                'skills': [],
                'experience': []
            },
            TypeError,
            None,
            ({'error': 'bad input data'}, 400)
    ),
    (
            {
                'firstname': 'no skills',
                'lastname': 'User',
                'experience': [
                    {
                        'company': 'Firma',
                        'project': 'Project',
                        'duration': 5
                    }]
            },
            None,
            AttributeError,
            ({'error': 'bad input data'}, 400)
    ),
    (
            {
                'username': 'aaa',
                'firstname': 'no skills',
                'lastname': 'User',
                'skills': [],
                'experience': []
            },
            OperationalError('', '', ''),
            None,
            ({'error': 'db error'}, 500)
    ),
    (
            {},
            None,
            None,
            ({'error': 'bad input data'}, 400)
    )
])
@patch('app.auth.extract_user')
@patch('app.main.get_session')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_api_post_cv(replace_experience_with_json_mock, replace_skills_with_json_mock, get_session_mock,
                     extract_user_mock,
                     api_cv_post, client,
                     test_input, replace_skills_with_json_error, replace_experience_with_json_error,
                     expected):
    if replace_skills_with_json_error is not None:
        replace_skills_with_json_mock.side_effect = replace_skills_with_json_error
    if replace_experience_with_json_error is not None:
        replace_experience_with_json_mock.side_effect = replace_experience_with_json_error

    extract_user_mock.return_value = User(username='test', password='test', firstname='te', lastname='st', admin=True)

    response = client.post('/api/cv', json=test_input, follow_redirects=True)

    actual = response.get_json(), response.status_code

    assert actual == expected


@patch('app.auth.extract_user')
@patch('app.main.get_session')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_api_post_cv_data_error(replace_skills_with_json_mock, replace_experience_with_json_mock, get_session_mock,
                                extract_user_mock,
                                api_cv_post, client):
    session = get_session_mock()
    session.commit.side_effect = DataError

    extract_user_mock.return_value = User(username='test', password='test', firstname='te', lastname='st', admin=True)

    response = client.post('/api/cv', json={}, follow_redirects=True)
    actual = response.get_json(), response.status_code
    assert actual == ({'error': 'bad input data'}, 400)


@patch('app.auth.extract_user')
@patch('app.main.get_session')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
@pytest.mark.parametrize('token_error, expected', [
    (
            ExpiredTokenError,
            ({'message': 'token has expired'}, 401),
    ),
    (
            InvalidTokenError,
            ({'message': 'token is invalid'}, 401)
    ),
    (
            MissingTokenError,
            ({'message': 'token is missing'}, 401)
    ),
])
def test_api_post_cv_token_error(replace_skills_with_json_mock, replace_experience_with_json_mock, get_session_mock,
                                 extract_user_mock,
                                 api_cv_post, client, token_error, expected):
    extract_user_mock.side_effect = token_error

    response = client.post('/api/cv', json={}, follow_redirects=True)
    actual = response.get_json(), response.status_code
    assert actual == expected
