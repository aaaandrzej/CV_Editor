from behave import step
import requests
from features.environment import APP_URL


@step('an app is running')
def step_impl(context):
    health_check = requests.get(APP_URL)
    assert health_check.status_code == 200, \
        f'actual: {health_check.status_code}, expected: 200'
