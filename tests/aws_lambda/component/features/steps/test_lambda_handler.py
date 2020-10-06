import json
from pathlib import Path

from behave import step

from aws_lambda.main import handler
from aws_lambda.models import User
from tests.aws_lambda.component.environment import get_session

fixtures_dir = 'tests/aws_lambda/component/fixtures/'


@step('DB is up')
def step_impl(context):
    session = get_session()
    db_health_check = session.connection()
    assert db_health_check is not None, \
        f'actual: {db_health_check}, expected: not None'


@step('user sends "{json_file}" query')
def step_impl(context, json_file):
    with open(Path(fixtures_dir) / json_file) as file:
        payload = json.load(file)

    event = {'body': json.dumps(payload)}
    cntxt = ''

    context.handler_output = handler(event, cntxt)


@step('they should get a "{response}" response')
def step_impl(context, response):
    assert str(context.handler_output) == response, \
        f'actual: {str(context.handler_output)}, expected: {response}'


@step('"{json_file}" content is present in database')
def step_impl(context, json_file):

    with open(Path(fixtures_dir) / json_file) as file:
        payload = json.load(file)

    validated_user = {
        'firstname': payload['firstname'],
        'lastname': payload['lastname'],
        'skills': payload.get('skills', ''),
        'experience': payload.get('experience', [])
    }

    session = get_session()
    context.response = [user.object_as_dict() for user in session.query(User).all()]

    assert validated_user in context.response, \
        f'actual: {validated_user}, in expected: {context.response}'
