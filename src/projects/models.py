from django.db import models


class Project(models.Model):
    """Project"""
    title = models.CharField(max_length=500)
    summary = models.CharField(blank=True, max_length=500)

    project_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
