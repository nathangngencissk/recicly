import json

import requests

from model import Car
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    car = Car(**body)

    db = Database()

    updated_car = db.update(Car)

    updated_car.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'car': updated_car.__dict__,
            'msg': f'Car {updated_car.id} updated successfully'
        }),
    }

    return response
