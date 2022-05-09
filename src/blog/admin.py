from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'visibility', 'published')
    sortable_by = ()
