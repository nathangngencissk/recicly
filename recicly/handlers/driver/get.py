import json

from utils.database import Database
from model.driver import Driver


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    driver = db.get(Driver, id=id, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(driver),
    }

    return response
