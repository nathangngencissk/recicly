import collections

from datetime import date, datetime, timedelta
from decimal import Decimal


def object_to_dict(element):
    return {c.name: getattr(element, c.name) for c in element.__table__.columns}


def flatten(d, parent_key='', sep='.'):
    """Flattens a dictionary"""

    items = []

    for k, v in d.items():

        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, collections.MutableMapping):

            items.extend(flatten(v, new_key, sep=sep).items())

        else:

            items.append((new_key, v))

    return dict(items)


def update(d, u):

    for k, v in u.items():

        if isinstance(v, collections.abc.Mapping):

            d[k] = update(d.get(k, {}), v)

        else:

            d[k] = v

    return d


def formatter(object):
    """Default json formatter"""

    if isinstance(object, (dict, collections.defaultdict)):

        for key, value in object.items():

            object[key] = formatter(value)

        return object

    elif isinstance(object, list):

        return [formatter(item) for item in object]

    elif isinstance(object, set):

        return {formatter(item) for item in object}

    elif isinstance(object, datetime):

        return object.strftime('%Y-%m-%d %H:%M:%S.%f')

    elif isinstance(object, date):

        return object.strftime('%Y-%m-%d')

    elif isinstance(object, Decimal):

        if object % 1 == 0:

            return int(object)

        else:

            return f'{object:.8f}'

    elif isinstance(object, bytes):

        return object.decode(errors='ignore')

    elif isinstance(object, timedelta):

        return str(object)

    else:

        return object
