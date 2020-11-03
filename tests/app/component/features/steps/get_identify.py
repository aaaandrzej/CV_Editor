from behave import when, then, step
import requests
from urllib.parse import urljoin
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User
from tests.app.component.environment import APP_URL, get_session


@step('db is up')
def step_impl(context):
    context.session = get_session()
    db_health_check = context.session.connection()
    assert db_health_check is not None, \
        f'actual: {db_health_check}, expected: not None'


@step('db contains a user record')
def step_impl(context):
    context.admin_user = User(username='admin',
                              password=generate_password_hash('nimda', method='sha256', salt_length=8),
                              firstname='ad',
                              lastname='min',
                              admin=True)

    if not context.session.query(User).filter_by(username=context.admin_user.username).first():
        context.session.add(context.admin_user)
        context.session.commit()

    admin_in_db = context.session.query(User).filter_by(username='admin').one()

    assert (context.admin_user.username, context.admin_user.firstname, context.admin_user.lastname) == (
        admin_in_db.username, admin_in_db.firstname, admin_in_db.lastname), \
        f'actual: {(context.admin_user.username, context.admin_user.firstname, context.admin_user.lastname)}, expected: {(admin_in_db.username, admin_in_db.firstname, admin_in_db.lastname)}'


@step('user requests new token')
def step_impl(context):
    url = urljoin(APP_URL, 'login')

    response = requests.get(url, auth=('admin', 'nimda'))
    context.token = response.json()['token']

    assert len(context.token) == 131, \
        f'actual: {len(context.token)}, expected: {131}'


@step('user uses get method with token attached on identify endpoint')
def step_impl(context):
    url = urljoin(APP_URL, 'identify')

    context.endpoint_response = requests.get(url, headers={'Authorization': f'Bearer {context.token}'})

    assert context.endpoint_response is not None, \
        f'actual: {context.endpoint_response}, expected not None'


@then('they should receive a "200" status code')
def step_impl(context):

    context.status_code = context.endpoint_response.status_code

    assert context.status_code == 200, \
        f'actual: {context.status_code}, expected {200}'


@step('a message response is json with admin user details')
def step_impl(context):

    context.response = context.endpoint_response.json()

    assert (context.admin_user.username, context.admin_user.firstname, context.admin_user.lastname) == (
        context.response['username'], context.response['firstname'], context.response['lastname']), \
        f"actual: {(context.admin_user.username, context.admin_user.firstname, context.admin_user.lastname)}, \
        expected: {(context.response['username'], context.response['firstname'], context.response['lastname'])}"
