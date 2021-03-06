import json

import requests

from model import Collector
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    collector = Collector(**body)

    db = Database()

    db.add(collector)

    collector.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps({
            'collector': collector.__dict__,
            'msg': f'Collector {collector.id} added successfully'
        }),
    }

    return response
