import json

from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, CreateView

from httpbucket import forms
from . import models


def hello_world(request):
    return HttpResponse("Obligatory greeting!")


class EchoView(View):
    http_method_names = ['get']

    def get(self, request):
        response = {}

        # Add what we know we can always get from the request
        response['origin'] = request.META.get('REMOTE_ADDR')
        response['url'] = request.get_raw_uri()

        # Add any query parameters found in the URI
        args = {}
        for k, v in request.GET.lists():
            if len(v) == 1:
                args[k] = v[0]
            else:
                args[k] = v
        response['args'] = args

        # Add any headers we find in the request
        headers = {}
        for k, v in request.META.items():
            if not v:
                continue
            new_key = None

            # Content-Type and Content-Location aren't modified
            if k.startswith("CONTENT"):
                new_key = k
            # Any other headers in the request are prepended with HTTP_
            elif k.startswith('HTTP_'):
                new_key = k[5:]

            if new_key is not None:
                headers[new_key.replace('_', '-').title()] = v
        response['headers'] = headers

        request_log_entry = models.RequestLogEntry(
            method='GET',
            origin=response['origin'],
            uri=response['url'],
            headers=response['headers'],
            args=response['args'],
        )
        request_log_entry.save()

        return HttpResponse(json.dumps(response, sort_keys=True))


class RequestLogEntryDetailView(DetailView):
    model = models.RequestLogEntry


class RequestLogEntryCreateView(CreateView):
    model = models.RequestLogEntry
    form_class = forms.RequestLogEntryForm
