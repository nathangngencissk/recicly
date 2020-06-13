import json

from utils.database import Database
from utils import object_to_dict
from model import User


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    user = db.get(User, id=id)

    adresses = []

    for adress in user.adresses:
        adresses.append(object_to_dict(adress))

    response = {
        'statusCode': 200,
        'body': json.dumps(adresses),
    }

    return response
