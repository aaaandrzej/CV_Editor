from behave import when, then, step
import boto3

from tests.aws_lambda.component.environment import ENDPOINT_URL, REGION_NAME, \
    AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SECURITY_TOKEN, AWS_SESSION_TOKEN


@when('user uses get secret method')
def step_impl(context):

    conn = boto3.client('secretsmanager', region_name=REGION_NAME, endpoint_url=ENDPOINT_URL,
                        aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    try:
        create_secret = conn.create_secret(Name='test', SecretString='dupa')
    except conn.exceptions.ResourceExistsException:
        pass

    from aws_lambda.get_secret import get_secret

    context.result = get_secret(endpoint_url=ENDPOINT_URL, region_name=REGION_NAME, secret_name='test')


@then('they should receive a "dupa" response')
def step_impl(context):

    assert context.result == 'dupa', \
                     f'actual: {context.result}, expected: dupa'

