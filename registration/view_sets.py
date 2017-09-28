from django.contrib.auth import models as auth_models

from rest_framework import viewsets, permissions

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser,)
