import json

import requests

from model.driver import Driver
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    driver = Driver(**body)

    db = Database()

    db.add(driver)

    driver.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'user': driver.__dict__,
            'msg': f'Driver {driver.id} added successfully'
        }),
    }

    return response
