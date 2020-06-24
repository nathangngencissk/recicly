import json

from model import Request


def handle(event, context):

    new_requests = Request.get_requests_in_evaluation()

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(new_requests),
    }

    return response
