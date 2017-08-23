from django.db import models


class RequestLogEntry(models.Model):
    class Meta:
        verbose_name_plural = "Request log entries"

    # we get `id` field as Primary Key by default

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
