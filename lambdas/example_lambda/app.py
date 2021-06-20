import json
import secrets_manager_generator as secrets_manager_generator
import os

print("Setup Started")

aws_key = os.environ["AWS_ACCESS_KEY_ID"]
aws_secret = os.environ["AWS_SECRET_ACCESS_KEY"]
environment = os.environ["environment"]
secrets_manager_client = secrets_manager_generator.get_secret_client(environment,aws_key,aws_secret)

print("Setup Started")


def lambda_handler(event, context):
    print("Entered Function")
    secrets_manager_name = os.environ["secretsmanager_name"]
    my_secret = secrets_manager_client.get_secret_value(SecretId=secrets_manager_name)
    print(f"Secret String value: {my_secret['SecretString']}")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        })
    }
