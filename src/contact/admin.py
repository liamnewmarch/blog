from django.contrib import admin

from . import models


@admin.register(models.Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'datetime')
    sortable_by = ()
