import json

from utils.database import Database
from model import Collector


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    id = queryStringParameters.get('id')

    db = Database()

    collector = db.get(Collector, id=id, as_dict=True)

    response = {
        'statusCode': 200,
        'body': json.dumps(collector),
    }

    return response
