from json import JSONDecodeError
from behave import step
import requests, json
from urllib.parse import urljoin
from pathlib import Path
from tests.app.component.environment import APP_URL

fixtures_dir = 'tests/app/component/fixtures/'


@step('admin user sends "{json_file}" query')
def step_impl(context, json_file):
    with open(Path(fixtures_dir) / json_file) as file:
        context.payload = json.load(file)

    url = urljoin(APP_URL, 'api/cv')

    try:
        context.token
    except AttributeError:
        context.token = ''

    context.endpoint_response = requests.post(url, json=context.payload, headers={'Authorization': f'Bearer {context.token}'})

    assert context.endpoint_response.status_code != 500, \
        f'actual: {context.endpoint_response.status_code}, expected not 500'


@step('"{json_file}" content is present in database')
def step_impl(context, json_file):

    url = urljoin(APP_URL, 'api/cv')

    verification_response = requests.get(url)
    context.verification_response = verification_response.json()

    assert context.payload['username'] in [user['username'] for user in context.verification_response], \
        f"actual: {context.payload['username']}, in expected: {[user['username'] for user in context.verification_response]}"


@step('a message response is "{response}"')
def step_impl(context, response):

    try:
        context.response = json.dumps(context.endpoint_response.json())
    except JSONDecodeError:
        context.response = context.endpoint_response.text
    assert context.response == response, \
        f'actual: {context.response}, expected: {response}'
