from unittest.mock import patch

import boto3
import json
import pytest
from moto import mock_secretsmanager
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import DataError


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
    {'body': '{"firstname": "Test", "lastname": "1", "skills": [], "experience": []}', 'statusCode': 200}
# ),
# (
#     {
#     'firstname': 'Second Test',
#     'lastname': 'User',
#     'skills': [
#         {
#         'skill_name': 'skill1',
#         'skill_level': 1
#         },
#         {
#         'skill_name': 'skill2',
#         'skill_level': 2
#         }],
#     'experience': [
#         {
#         'company': 'Firma',
#         'project': 'Project',
#         'duration': 5
#         }]
#     },
#     None,
#     None,
#     ({'success': 'item added'}, 201)
# ),
# (
#     {
#     'firstname': '3rd Test',
#     'lastname': 'User',
#     'dummy_key': 'doesnt matter',
#     'skills': [],
#     'experience': [
#         {
#         'company': 'Firma',
#         'project': 'Project',
#         'duration': 5
#         }]
#     },
#     None,
#     None,
#     ({'success': 'item added'}, 201)
# ),
# (
#     {
#     'firstname': '3rd Test',
#     'lastname': 'User',
#     'dummy_key': 'doesnt matter',
#     'skills': [],
#     'experience': [
#         {
#         'company': 'Firma',
#         'project': 'Project',
#         'duration': 5
#         },
#         {
#         'company': 'Firma2',
#         'project': 'Project',
#         'duration': 5
#         },
#         {
#         'company': 'Firma3',
#         'project': 'Project',
#         'duration': 5
#         }]
#     },
#     None,
#     None,
#     ({'success': 'item added'}, 201)
# ),
# (
#     {
#     'firstname': 'no exp',
#     'lastname': 'User',
#     'dummy_key': 'doesnt matter',
#     'skills': []
#     },
#     None,
#     None,
#     ({'success': 'item added'}, 201)
# ),
# (
#     {
#     'lastname': 'no firstname',
#     'skills': [],
#     'experience': []
#     },
#     KeyError,
#     KeyError,
#     ({'error': 'bad input data'}, 400)
# ),
# (
#     {
#     'firstname': 'no',
#     'lastname': 'no',
#     'skills': [],
#     'experience': []
#     },
#     TypeError,
#     None,
#     ({'error': 'bad input data'}, 400)
# ),
# (
#     {
#     'firstname': 'no skills',
#     'lastname': 'User',
#     'experience': [
#         {
#         'company': 'Firma',
#         'project': 'Project',
#         'duration': 5
#         }]
#     },
#     None,
#     AttributeError,
#     ({'error': 'bad input data'}, 400)
# ),
# (
#     {
#     'firstname': 'no skills',
#     'lastname': 'User',
#     'skills': [],
#     'experience': []
#     },
#     OperationalError('', '', ''),
#     None,
#     ({'error': 'db error'}, 500)
# ),
# (
#     {},
#     None,
#     None,
#     ({'error': 'bad input data'}, 400)
)
])
@patch('aws_lambda.main.get_session')
@patch('aws_lambda.functions.replace_skills_with_json')
@patch('aws_lambda.functions.replace_experience_with_json')
def test_api_post_cv(replace_experience_with_json_mock, replace_skills_with_json_mock, get_session_mock,
                     db_credentials,
                     test_input, replace_skills_with_json_error, replace_experience_with_json_error,
                     expected):

    if replace_skills_with_json_error is not None:
        replace_skills_with_json_mock.side_effect = replace_skills_with_json_error
    if replace_experience_with_json_error is not None:
        replace_experience_with_json_mock.side_effect = replace_experience_with_json_error

    from aws_lambda.main import handler

    event = {'body': json.dumps(test_input)}
    context = ''

    actual = handler(event, context)

    assert actual == expected
