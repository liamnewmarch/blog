from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Project


class ProjectTestCase(TestCase):
    fixtures = ('fixtures/placeholder.yaml',)

    def test_project_fixture(self):
        self.assertEqual(Project.objects.count(), 1)

    def test_project_project_url_must_be_valid(self):
        project = Project(title='Test project_url')
        with self.assertRaises(ValidationError):
            project.project_url = 'Not a URL'
            project.full_clean()

    def test_project_source_url_must_be_valid(self):
        project = Project(title='Test source_url')
        with self.assertRaises(ValidationError):
            project.source_url = 'Not a URL'
            project.full_clean()
