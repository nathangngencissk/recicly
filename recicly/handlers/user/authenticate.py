import json

import requests

from model import User


def handle(event, context):
    body = json.loads(event.get('body'))

    email = body.get('email')
    password = body.get('password')

    result = User.authenticate(email, password)

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
