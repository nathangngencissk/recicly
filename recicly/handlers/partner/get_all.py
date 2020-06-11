import json

from utils.database import Database
from model import Partner


def handle(event, context):
    db = Database()
    partner = db.get_all(Partner, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(partner),
    }

    return response
