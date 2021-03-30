from django.core.exceptions import ValidationError
from django.db import models


class Home(models.Model):
    """Home page singular model."""
    title = models.CharField(max_length=500)
    intro = models.CharField(max_length=500)

    featured_project_1 = models.OneToOneField(
        'projects.Project',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='+',
    )

    featured_project_2 = models.OneToOneField(
        'projects.Project',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='+',
    )

    featured_project_3 = models.OneToOneField(
        'projects.Project',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='+',
    )

    @property
    def featured_projects(self):
        if self.featured_project_1:
            yield self.featured_project_1
        if self.featured_project_2:
            yield self.featured_project_2
        if self.featured_project_3:
            yield self.featured_project_3

    def __str__(self):
        return Home.__name__

    def clean(self, *args, **kwargs):
        # If there’s already an instance of Home the add permission should be
        # disabled in the ModelAdmin but lets validate anyway.
        if Home.objects.count() > 0 and Home.objects.get().id != self.id:
            raise ValidationError('A home page instance already exists')

        return super().clean(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'home'  # There should only be one instance.
