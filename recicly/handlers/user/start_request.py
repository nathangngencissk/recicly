import json

import requests

from model import User
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    user_id = body.get('user_id')
    address_id = body.get('address_id')

    db = Database()

    user = db.get(User, user_id)

    result = user.start_request(address_id)

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
