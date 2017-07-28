import json

from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Obligatory greeting!")


def echo_get(request):
    response = {}

    args = {}
    for k, v in request.GET.lists():
        if len(v) == 1:
            args[k] = v[0]
        else:
            args[k] = v
    response['args'] = args

    headers = {}
    for k, v in request.META.items():
        if not v:
            continue
        new_key = None
        if k.startswith("CONTENT"):
            new_key = k
        elif k.startswith('HTTP_'):
            new_key = k[5:]
        if new_key is not None:
            headers[new_key.replace('_', '-').title()] = v
    response['headers'] = headers

    response['origin'] = request.META.get('REMOTE_ADDR')
    response['url'] = request.get_raw_uri()

    return HttpResponse(json.dumps(response, sort_keys=True))
