from behave import step
import requests, json
from urllib.parse import urljoin
from pathlib import Path
from tests.component.environment import APP_URL

fixtures_dir = 'tests/component/fixtures/'


@step('user sends "{json_file}" query')
def step_impl(context, json_file):
    with open(Path(fixtures_dir) / json_file) as file:
        payload = json.load(file)

    url = urljoin(APP_URL, 'api/cv')

    response = requests.post(url, json=payload)
    context.response = response.json()
    context.status_code = response.status_code


@step('they should get a "{status_code}" status code')
def step_impl(context, status_code):
    assert context.status_code == int(status_code), \
        f'actual: {context.status_code}, expected: {int(status_code)}'


@step('a response message is "{response}"')
def step_impl(context, response):
    assert context.response == json.loads(response), \
        f'actual: {context.response}, expected: {json.loads(response)}'


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

    url = urljoin(APP_URL, 'api/cv')

    response = requests.get(url)
    context.response = response.json()

    assert validated_user in context.response, \
        f'actual: {validated_user}, in expected: {context.response}'
