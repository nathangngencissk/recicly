import json

from model import Request


def handle(event, context):

    new_requests = Request.get_new_requests()

    response = {
        'statusCode': 200,
        'body': json.dumps(new_requests),
    }

    return response
