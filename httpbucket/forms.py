import logging

from django import forms

from . import models

logger = logging.getLogger(__name__)


class RequestLogEntryForm(forms.ModelForm):
    class Meta:
        model = models.RequestLogEntry
        exclude = ['id']
