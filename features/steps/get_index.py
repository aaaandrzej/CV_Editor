from behave import given, when, then, step
import requests


@given('an app is running')
def step_impl(context):
    pass


@when('user uses get method on index endpoint')
def step_impl(context):
    response = requests.get('http://127.0.0.1:5000/')  # TODO podmienic na env var
    context.response = response.text
    context.status_code = response.status_code


@then('they should receive a "{status_code}" status code')
def step_impl(context, status_code):
    assert context.status_code == int(status_code)


@then('a message response is "{response}"')
def step_impl(context, response):
    assert context.response == response,\
        f'actual: {context.response}, expected: {response}'
