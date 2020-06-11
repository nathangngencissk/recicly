import json

from utils.database import Database
from utils import object_to_dict
from model import Adress


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    adress = db.get(Adress, id=id)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'product': object_to_dict(adress)
        })
    }

    return response
