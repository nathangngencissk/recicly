import json

from utils.database import Database
from utils import object_to_dict
from model import Adress, User


def handle(event, context):
    db = Database()
    adresses = []

    for adress in db.get_all(Adress, as_dict=True):
        if adress.get('id_collector'):
            adress.append({
                'adress': adress,
                'collector': object_to_dict(adress.collector)
            })
        else:
            user = db.get(User, adress.id_user)
            adress.append({
                'adress': adress,
                'user': object_to_dict(user)
            })

    response = {
        'statusCode': 200,
        'body': json.dumps(adresses),
    }

    return response
