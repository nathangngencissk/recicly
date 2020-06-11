import json

import requests

from model import User
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    user = User(**body)

    db = Database()

    db.add(user)

    user.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'user': user.__dict__,
            'msg': f'User {user.id} added successfully'
        }),
    }

    return response
