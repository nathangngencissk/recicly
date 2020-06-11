import json

import requests

from model import Adress
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    adress = Adress(**body)

    db = Database()

    updated_adress = db.update(adress)

    updated_adress.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'adress': updated_adress.__dict__,
            'msg': f'Adress {updated_adress.id} updated successfully'
        }),
    }

    return response
