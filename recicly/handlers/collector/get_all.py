import json

from utils.database import Database
from model import Collector


def handle(event, context):
    db = Database()
    collectors = db.get_all(Collector, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(collectors),
    }

    return response
