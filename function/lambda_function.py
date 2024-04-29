import os
import logging
import jsonpickle
import boto3

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

client = boto3.client('lambda')
client.get_account_settings()

def lambda_handler(event, context: LambdaContext) -> str:
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))
    response = client.get_account_settings()
    return response['AccountUsage']
