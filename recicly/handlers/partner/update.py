import json

import requests

from model import Partner
from utils.database import Database


def handle(event, context):
    body = json.loads(event.get('body'))

    partner = Partner(**body)

    db = Database()

    updated_partner = db.update(partner)

    updated_partner.__dict__.pop('_sa_instance_state')

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'partner': updated_partner.__dict__,
            'msg': f'Partner {updated_partner.id} updated successfully'
        }),
    }

    return response
