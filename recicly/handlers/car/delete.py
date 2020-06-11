import json

import requests

from model.driver import Car
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    car = Car(id=id)

    db = Database()

    db.delete(car)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'Car with id {id} deleted successfully'
        }),
    }

    return response
