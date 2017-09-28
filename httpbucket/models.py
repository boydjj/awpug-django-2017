from django.conf import settings
from django.db import models
from django.urls import reverse


class RequestLogEntry(models.Model):
    class Meta:
        verbose_name_plural = "Request log entries"

    # we get `id` field as Primary Key by default

    # keep track of which user created this
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # OPTIONS is the longest method name
    method = models.CharField(max_length=7)

    # probably max of 2000 chars, but why limit it?
    uri = models.TextField()

    # some fields are specialized!
    origin = models.GenericIPAddressField()

    # just a JSON blob
    headers = models.TextField()

    # another JSON blob
    args = models.TextField()

    def get_absolute_url(self):
        return reverse('replay_get', kwargs={'pk': self.id})
