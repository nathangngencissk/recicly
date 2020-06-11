import json

import requests

from model import Driver
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    driver = Driver(id=id)

    db = Database()

    db.delete(driver)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'Driver with id {id} deleted successfully'
        }),
    }

    return response
