import json

from utils.database import Database
from model import User, Product


def handle(event, context):

    body = json.loads(event.get('body'))

    user_id = body.get('user_id')
    product_id = body.get('product_id')

    db = Database()

    user = db.get(User, id=user_id)

    order = user.exchange_points(product_id=product_id)

    response = {
        'statusCode': 200,
        'body': json.dumps(order),
    }

    return response
