import json

import requests

from model import Product
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    product = Product(**body)

    db = Database()

    db.add(product)

    product.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'product': product.__dict__,
            'msg': f'Product {product.id} added successfully'
        }),
    }

    return response
