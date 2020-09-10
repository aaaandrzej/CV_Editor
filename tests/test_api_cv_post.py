from unittest.mock import patch, Mock
import pytest
from sqlalchemy.exc import OperationalError


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
    'firstname': 'Test',
    'lastname': '1',
    'skills': [],
    'experience': []
    },
    None,
    None,
    ({'success': 'item added'}, 201)
),
(
    {
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
    ({'success': 'item added'}, 201)
),
(
    {
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
    ({'success': 'item added'}, 201)
),
(
    {
    'firstname': '3rd Test',
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
    ({'success': 'item added'}, 201)
),
(
    {
    'firstname': 'no exp',
    'lastname': 'User',
    'dummy_key': 'doesnt matter',
    'skills': []
    },
    None,
    None,
    ({'success': 'item added'}, 201)
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
    KeyError,
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
    KeyError,
    ({'error': 'bad input data'}, 400)
),
# TODO to ponizej nie zadziala:
# (
#     {
#     'firstname': 'no skills',
#     'lastname': 'User',
#     'skills': [],
#     'experience': []
#     },
#     None,
#     OperationalError,
#     ({'error': 'db error'}, 500)
# ),
(
    {},
    None,
    None,
    ({'error': 'bad input data'}, 400)
)
])
@patch('app.main.get_session')
@patch('app.main.replace_skills_with_json')
@patch('app.main.replace_experience_with_json')
def test_api_post_cv(replace_skills_with_json_mock, replace_experience_with_json_mock, get_session_mock,
                                test_input, replace_skills_with_json_error, replace_experience_with_json_error,
                                expected,
                                api_cv_post, client):
    client.post('/api/cv', json=test_input)  # TODO docelowo mozna zamienic na json=Mock()
    if replace_skills_with_json_error is not None:
        replace_skills_with_json_mock.side_effect = replace_skills_with_json_error
    if replace_experience_with_json_error is not None:
        replace_experience_with_json_mock.side_effect = replace_experience_with_json_error

    actual = api_cv_post()

    assert actual == expected


# TODO IN PROGRESS
# @patch('app.session.session')
# def test_api_cv_post_no_db_error(session_mock, client, api_cv_post, test_input={
#     'firstname': 'Test',
#     'lastname': 'User',
#     'skills': [],
#     'experience': []
# }):
#     actual = client.post('/api/cv', json=test_input)
#     session_mock.side_effect = OperationalError
#     # actual = api_cv_post()
#     expected = ({'error': 'db error'}, 500)
#     assert actual == expected
