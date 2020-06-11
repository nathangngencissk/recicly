import json

from utils.database import Database
from utils import object_to_dict
from model import Product


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    product = db.get(Product, id=id)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'product': object_to_dict(product),
            'partner': object_to_dict(product.partner)
        }),
    }

    return response
