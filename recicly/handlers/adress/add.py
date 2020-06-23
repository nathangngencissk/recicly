import json

import requests

from model import Adress
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    adress = Adress(**body)

    db = Database()

    db.add(adress)

    adress.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'adress': adress.__dict__,
            'msg': f'Adress {adress.id} added successfully'
        }),
    }

    return response
