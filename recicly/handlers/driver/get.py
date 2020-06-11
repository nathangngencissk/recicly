import json

from utils.database import Database
from utils import object_to_dict
from model import Driver


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    driver = db.get(Driver, id=id)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'driver': object_to_dict(driver),
            'cars': driver.get_cars()
        }),
    }

    return response
