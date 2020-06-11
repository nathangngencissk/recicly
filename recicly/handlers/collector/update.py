import json

import requests

from model.collector import Collector
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    collector = Collector(**body)

    db = Database()

    updated_collector = db.update(collector)

    updated_collector.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'collector': updated_collector.__dict__,
            'msg': f'Collector {updated_collector.id} updated successfully'
        }),
    }

    return response
