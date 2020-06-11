import json

import requests

from model import User
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    user = User(**body)

    db = Database()

    updated_user = db.update(user)

    updated_user.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'user': updated_user.__dict__,
            'msg': f'User {updated_user.id} updated successfully'
        }),
    }

    return response
