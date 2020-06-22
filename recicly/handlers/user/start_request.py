import json

import requests

from model import User
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    db = Database()

    user = db.get(User, id)

    result = user.start_request()

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
