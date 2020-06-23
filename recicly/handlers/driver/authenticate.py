import json

import requests

from model import Driver


def handle(event, context):
    body = json.loads(event.get('body'))

    email = body.get('email')
    password = body.get('password')

    result = Driver.authenticate(email, password)

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
