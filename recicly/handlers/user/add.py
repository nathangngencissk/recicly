import json

import requests

from model.user import User


def handle(event, context):
    body = event.get('body')
    print(body)
    # new_user = User(**user)

    response = {
        'statusCode': 200,
        'body': json.dumps(body),
    }

    return response
