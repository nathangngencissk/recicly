import json

from model import Collector


def handle(event, context):

    queryStringParameters = event.get('queryStringParameters')

    code = queryStringParameters.get('code')

    collector = Collector.get_from_code(code)

    response = {
        'statusCode': 200,
        'body': json.dumps(collector),
    }

    return response
