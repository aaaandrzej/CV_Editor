from behave import given, when, then, step
import requests, json
from features.environment import APP_URL


@step('an app is still running')
def step_impl(context):
    health_check = requests.get(APP_URL)
    assert health_check.status_code == 200, \
        f'actual: {health_check.status_code}, expected: 200'


@step('user sends "{json_input}" query')
def step_impl(context, json_input):
    payload = {"firstname": "",
               "lastname": "",
               "skills": [],
               "experience": []}
    url = APP_URL + 'api/cv'
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
