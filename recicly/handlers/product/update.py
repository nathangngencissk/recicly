import json

import requests

from model import Product
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    product = Product(**body)

    db = Database()

    updated_product = db.update(product)

    updated_product.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'product': updated_product.__dict__,
            'msg': f'Product {updated_product.id} updated successfully'
        }),
    }

    return response
