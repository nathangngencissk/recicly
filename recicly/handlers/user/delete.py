import json

import requests

from model.user import User
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    user = User(id=id)

    db = Database()

    db.delete(user)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'User with id {id} deleted successfully'
        }),
    }

    return response
