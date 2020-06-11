import json

from utils.database import Database
from model import Car


def handle(event, context):
    db = Database()
    cars = db.get_all(Car, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(cars),
    }

    return response
