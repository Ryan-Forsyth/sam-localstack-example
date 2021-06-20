import boto3

def get_secret_client(environment,aws_key,aws_secret):
    local_url = "http://host.docker.internal:4566"
    current_url = local_url if environment == 'local' else None

    session = boto3.session.Session()
    return session.client(
        service_name='secretsmanager',
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret,
        endpoint_url=current_url
    )
