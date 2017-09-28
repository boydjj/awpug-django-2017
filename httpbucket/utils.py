import json


def model_to_dict(model_obj):
    return {
        'id': model_obj.id,
        'method': model_obj.method,
        'origin': model_obj.origin,
        'uri': model_obj.uri,
        'headers': json.loads(model_obj.headers),
        'args': json.loads(model_obj.args)
    }
