import json

from utils.database import Database
from utils import object_to_dict
from model import Partner


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    partner = db.get(Partner, id=id)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'partner': object_to_dict(partner),
            'products': partner.get_products()
        }),
    }

    return response
