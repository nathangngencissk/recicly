import json

from utils.database import Database
from utils import object_to_dict
from model import Product


def handle(event, context):
    db = Database()
    products = []

    for product in db.get_all(Product):
        products.append({
            'product': object_to_dict(product),
            'partner': object_to_dict(product.partner)
        })

    response = {
        'statusCode': 200,
        'body': json.dumps(products),
    }

    return response
