from rest_framework import serializers

from . import models


class RequestLogEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RequestLogEntry
        fields = ('user', 'method', 'uri', 'origin', 'headers', 'args', 'url', 'user')
