import json

from utils.database import Database
from model import User


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    user = db.get(User, id=id)

    requests = user.get_requests()

    response = {
        'statusCode': 200,
        'body': json.dumps(requests),
    }

    return response
