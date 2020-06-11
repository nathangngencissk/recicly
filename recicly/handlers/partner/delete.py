import json

import requests

from model import Partner
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    partner = Partner(id=id)

    db = Database()

    db.delete(partner)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'Partner with id {id} deleted successfully'
        }),
    }

    return response
