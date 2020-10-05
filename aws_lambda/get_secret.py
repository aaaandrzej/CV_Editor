import boto3


def get_secret(region_name='us-east-2', secret_name='haslo', endpoint_url=None):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        endpoint_url=endpoint_url
    )

    get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

    # Your code goes here.
    return get_secret_value_response['SecretString']
