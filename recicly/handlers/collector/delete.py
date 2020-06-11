import json

import requests

from model import Collector
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    collector = Collector(id=id)

    db = Database()

    db.delete(collector)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'Collector with id {id} deleted successfully'
        }),
    }

    return response
