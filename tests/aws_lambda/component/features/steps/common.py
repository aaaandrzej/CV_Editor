
from behave import step
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

from tests.aws_lambda.component.environment import REGION_NAME, ENDPOINT_URL


@step('localstack is running')
def step_impl(context):
    try:
        s3 = boto3.resource('s3', endpoint_url=ENDPOINT_URL)
        health_check_bucket = s3.create_bucket(Bucket='health-check-bucket')
        s3.meta.client.head_bucket(Bucket='health-check-bucket')
        health_check = True
    except(EndpointConnectionError, ClientError):
        health_check = False

    assert health_check is True, \
        f'actual: {health_check}, expected: True'
