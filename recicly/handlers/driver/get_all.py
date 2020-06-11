import json

from utils.database import Database
from model.driver import Driver


def handle(event, context):
    db = Database()
    drivers = db.get_all(Driver, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(drivers),
    }

    return response
