import json

import requests

from model import Collector
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    collector_id = body.get('collector_id')
    request_id = body.get('request_id')
    weight = body.get('weight')

    db = Database()

    collector = db.get(Collector, collector_id)

    response = collector.evaluate_request(id_request=request_id, weight=weight)

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(response),
    }

    return response
