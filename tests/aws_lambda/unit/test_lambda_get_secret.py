import boto3
from moto import mock_secretsmanager

from aws_lambda.get_secret import get_secret


@mock_secretsmanager
def test_get_secret_value(aws_credentials):
    conn = boto3.client("secretsmanager", region_name="us-east-2")
    create_secret = conn.create_secret(Name="haslo", SecretString="dupa")

    result = get_secret()

    assert result == "dupa"
