# sam-localstack-example

---
## Overview:
This code was created to demo how localstack and SAM can be used together for local
AWS development. This project uses docker to spin up localstack and relies on SAM 
to spin up and package and the lambda and lambda layers.

## Steps to run

1. Navigate to the [docker/localstack folder](docker/localstack) and run the following command.
This will bring the services mentioned in the service environment up. 
    ```shell
    docker-compose up
    ```
2. Navigate to the [scripts folder](scripts) and run the shell script using the following command
    ```shell
    ./setup-local-secrets-manager.sh
    ```
    This will create a secretsmanager resource locally and print its values to the user.
3. Run sam build and local invoke on the ExampleFunction
    - This will package and build the lambda layer and run the lambda locally.
    ```shell
      sam build ExampleFunction --template template.yaml
      sam local invoke ExampleFunction --template template.yaml --event events/event.json
    ```
   

**Note:** the code is a helloworld application that reaches out to secretsmanager and prints its values.
Normally this a bad thing to do, since secretsmanager is supposed to store confidential information.
However this application is meant to demonstrate how to run locally. This is not production.

The code that builds secretsmanager to run locally can be found in the 
[lambda layer](layers/secrets_manager_generator/secrets_manager_generator.py)

---
## More Info:
[LocalStack Github repo](https://github.com/localstack/localstack) 

[SAM CLI Documentation from AWS](https://aws.amazon.com/serverless/sam/)

---
## Quick Fixes / Known Issues

- SAM Lambdas can not connect to the host docker network
- Unable to find module x: If you are using pycharm, you may need to specify the lambdas and layers folders
as source roots folders.