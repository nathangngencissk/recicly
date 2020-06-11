import json

import requests

from model import Product
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    id = body.get('id')

    product = Product(id=id)

    db = Database()

    db.delete(product)

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'msg': f'Product with id {id} deleted successfully'
        }),
    }

    return response
