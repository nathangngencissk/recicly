import json

import requests

from model import Collector
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    collector_id = body.get('collector_id')

    db = Database()

    collector = db.get(Collector, collector_id)

    delivery_code = collector.receive_request()

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(delivery_code),
    }

    return response
