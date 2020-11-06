from urllib.parse import urljoin

from behave import step
import requests
from werkzeug.security import generate_password_hash

from app.models import User
from tests.app.component.environment import APP_URL, get_session

admin_user = User(username='admin',
                  password=generate_password_hash('nimda', method='sha256', salt_length=8),
                  firstname='ad',
                  lastname='min',
                  admin=True)

nonadmin_user = User(username='user',
                     password=generate_password_hash('resu', method='sha256', salt_length=8),
                     firstname='us',
                     lastname='er',
                     admin=False)


@step('an app is running')
def step_impl(context):
    health_check = requests.get(APP_URL)
    assert health_check.status_code == 200, \
        f'actual: {health_check.status_code}, expected: 200'


@step('db is up')
def step_impl(context):
    context.session = get_session()
    db_health_check = context.session.connection()
    assert db_health_check is not None, \
        f'actual: {db_health_check}, expected: not None'


@step('db contains "{user}" record')
def step_impl(context, user):

    if 'admin' in user:
        context.user = admin_user
    else:
        context.user = nonadmin_user

    if not context.session.query(User).filter_by(username=context.user.username).first():
        context.session.add(context.user)
        context.session.commit()

    user_in_db = context.session.query(User).filter_by(username=context.user.username).one()

    assert (context.user.username, context.user.firstname, context.user.lastname) == (
        user_in_db.username, user_in_db.firstname, user_in_db.lastname), \
        f'actual: {(context.user.username, context.user.firstname, context.user.lastname)}, \
        expected: {(user_in_db.username, user_in_db.firstname, user_in_db.lastname)}'


@step('user requests new token')
def step_impl(context):
    url = urljoin(APP_URL, 'login')

    login, password = context.user.username, context.user.username[::-1]
    response = requests.get(url, auth=(login, password))

    context.token = response.json()['token']
    context.header = {'Authorization': f'Bearer {context.token}'}

    assert len(context.token) == 131, \
        f'actual: {len(context.token)}, expected: {131}'


@step('user uses "{method}" method "{with_or_without_token}" token attached on "{endpoint}" endpoint')
def step_impl(context, method, with_or_without_token, endpoint):

    if endpoint == 'index':
        url = APP_URL
    else:
        url = urljoin(APP_URL, endpoint)

    if 'without' not in with_or_without_token:
        context.endpoint_response = requests.get(url, headers={'Authorization': f'Bearer {context.token}'})
    else:
        context.endpoint_response = requests.get(url)

    assert context.endpoint_response is not None, \
        f'actual: {context.endpoint_response}, expected not None'


@step('they should receive a "{status_code}" status code')
def step_impl(context, status_code):
    context.status_code = context.endpoint_response.status_code

    assert context.status_code == int(status_code), \
        f'actual: {context.status_code}, expected {status_code}'


@step('a message response is json with user details')
def step_impl(context):

    context.response = context.endpoint_response.json()

    try:
        context.payload
    except AttributeError:
        context.payload = context.user.object_as_dict()

    assert (context.payload['username'], context.payload['firstname'], context.payload['lastname']) == (
        context.response['username'], context.response['firstname'], context.response['lastname']), \
        f"actual: {(context.payload['username'], context.payload['firstname'], context.payload['lastname'])}, \
        expected: {(context.response['username'], context.response['firstname'], context.response['lastname'])}"
