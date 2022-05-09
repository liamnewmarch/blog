from django.core.exceptions import ValidationError
from django.db import models


class Home(models.Model):
    """Home page singular model."""
    title = models.CharField(max_length=500)
    intro = models.CharField(max_length=500)

    def __str__(self):
        return Home.__name__

    def clean(self):
        # If there’s already an instance of Home the add permission should be
        # disabled in the ModelAdmin but lets validate anyway.
        if Home.objects.count() and Home.objects.first().id != self.id:
            raise ValidationError('A home page instance already exists')

    class Meta:
        verbose_name_plural = 'home'  # There should only be one instance.
