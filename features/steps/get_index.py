from behave import given, when, then, step
import requests
from features.environment import APP_URL


@given('an app is running')
def step_impl(context):
    pass


@when('user uses get method on index endpoint')
def step_impl(context):
    response = requests.get(APP_URL)
    context.response = response.text
    context.status_code = response.status_code


@then('they should receive a "{status_code}" status code')
def step_impl(context, status_code):
    assert context.status_code == int(status_code)


@step('a message response is "{response}"')
def step_impl(context, response):
    assert context.response == response,\
        f'actual: {context.response}, expected: {response}'
