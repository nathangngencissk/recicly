import json

import requests

from model.driver import Driver
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    driver = Driver(**body)

    db = Database()

    updated_driver = db.update(driver)

    updated_driver.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'user': updated_driver.__dict__,
            'msg': f'Driver {updated_driver.id} updated successfully'
        }),
    }

    return response
