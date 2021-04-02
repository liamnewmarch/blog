import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.functional import cached_property
from markdown import markdown


class Post(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=500)
    slug = models.SlugField(
        blank=True,
        help_text='Leave blank to auto generate from title',
        max_length=500,
        unique=True,
    )

    class Visibility(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        UNLISTED = 'unlisted', 'Unlisted'

    visibility = models.CharField(
        choices=Visibility.choices,
        default=Visibility.DRAFT,
        help_text=(
            'Draft posts are visible only to logged-in users, published posts '
            'are visible to all users, and unlisted posts are visible to all '
            'users but are  hidden from list pages.'
        ),
        max_length=500,
    )
    published = models.DateField(default=datetime.date.today)

    summary = models.CharField(blank=True, max_length=500)
    body_markdown = models.TextField(blank=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    @cached_property
    def body(self):
        return markdown(self.body_markdown, extensions=(
            'codehilite',
            'fenced_code',
        ))

    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={
            'slug': self.slug,
        })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
