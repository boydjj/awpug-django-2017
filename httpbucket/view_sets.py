from rest_framework import viewsets, permissions

from . import serializers

from . import models


class RequestLogEntryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RequestLogEntrySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return models.RequestLogEntry.objects.filter(user=self.request.user)
