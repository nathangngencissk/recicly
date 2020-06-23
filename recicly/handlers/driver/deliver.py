import json

import requests

from model import Driver
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    code = body.get('code')
    id_driver = body.get('id_driver')
    id_request = body.get('id_request')

    db = Database()

    driver = db.get(Driver, id_driver)

    result = driver.deliver_request(id_request=id_request, delivery_code=code)

    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
