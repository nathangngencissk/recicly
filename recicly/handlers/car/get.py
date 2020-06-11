import json

from utils.database import Database
from model import Car


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    car = db.get(Car, id=id, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(car)
    }

    return response
