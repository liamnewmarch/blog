from django.core.validators import ValidationError
from django.test import TestCase

from .models import Home


class HomeTestCase(TestCase):
    fixtures = ('fixtures/placeholder.yaml',)

    def test_home_fixture(self):
        self.assertEqual(Home.objects.count(), 1)

    def test_home_limited_to_one_instance(self):
        with self.assertRaises(ValidationError):
            home = Home(title="Bar", intro="Bar")
            home.full_clean()
