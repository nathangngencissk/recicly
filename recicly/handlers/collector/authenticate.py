import json

import requests

from model import Collector


def handle(event, context):
    body = json.loads(event.get('body'))

    email = body.get('email')
    password = body.get('password')

    result = Collector.authenticate(email, password)

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(result)
    }

    return response
