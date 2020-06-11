import json

import requests

from model import Adress
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    adress = Adress(id=id)

    db = Database()

    db.delete(adress)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'Adress with id {id} deleted successfully'
        }),
    }

    return response
