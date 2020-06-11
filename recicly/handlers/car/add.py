import json

import requests

from model import Car
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    car = Car(**body)

    db = Database()

    db.add(car)

    car.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'driver': car.__dict__,
            'msg': f'Car {car.id} added successfully'
        }),
    }

    return response
