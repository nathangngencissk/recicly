import json

from utils.database import Database
from model import Driver


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    driver = db.get(Driver, id=id)

    requests = driver.get_requests()

    response = {
        'statusCode': 200,
        'body': json.dumps(requests),
    }

    return response
