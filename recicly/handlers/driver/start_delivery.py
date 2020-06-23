import json

import requests

from model import Driver
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    driver_id = body.get('driver_id')
    request_id = body.get('request_id')

    db = Database()

    driver = db.get(Driver, driver_id)

    result = driver.attend_request(request_id)

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
