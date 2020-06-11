import json

from utils.database import Database
from model.user import User


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    user = db.get(User, id=id, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(user),
    }

    return response
