from django.contrib import admin

from . import models


class RequestLogEntryAdmin(admin.ModelAdmin):
    list_display = ('method', 'origin', 'uri')
    list_filter = ('method', 'origin')


admin.site.register(models.RequestLogEntry, RequestLogEntryAdmin)
