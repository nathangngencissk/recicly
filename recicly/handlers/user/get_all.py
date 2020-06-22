import json

from utils.database import Database
from model import User


def handle(event, context):
    db = Database()
    users = db.get_all(User, as_dict=True)

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(users),
    }

    return response
