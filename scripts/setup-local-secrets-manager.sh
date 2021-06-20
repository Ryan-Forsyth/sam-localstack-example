#!/usr/bin/env bash
fake_secret="{
  \"key\": \"MyAwesomekey\",
  \"secret\": \"MySecretKey\",
}"

secretsmanager_name="exampleSecretsManager"
echo "${secretsmanager_name}"
aws --endpoint-url=http://localhost:4566 secretsmanager delete-secret \
--secret-id "${secretsmanager_name}" \
--force-delete-without-recovery
aws --endpoint-url=http://localhost:4566 secretsmanager create-secret \
--name "${secretsmanager_name}" \
--secret-string "${fake_secret}"

results=$(aws --endpoint-url=http://localhost:4566 secretsmanager get-secret-value --secret-id "${secretsmanager_name}")
echo "${results}"