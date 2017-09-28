from rest_framework import viewsets

from . import serializers

from . import models


class RequestLogEntryViewSet(viewsets.ModelViewSet):
    queryset = models.RequestLogEntry.objects.all()
    serializer_class = serializers.RequestLogEntrySerializer
