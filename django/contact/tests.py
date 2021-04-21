from django.core.validators import ValidationError
from django.test import TestCase

from .models import Response


class ResponseTestCase(TestCase):
    def test_response_is_created_for_valid_data(self):
        response = Response.objects.create(
            name='Foo',
            email='foo@example.com',
            message='Foo message'
        )
        response.full_clean()

    def test_response_name_is_required(self):
        response = Response.objects.create(
            email='foo@example.com',
            message='Foo message'
        )
        with self.assertRaises(ValidationError):
            response.full_clean()

    def test_response_email_is_required(self):
        response = Response.objects.create(
            name='Foo',
            message='Foo message'
        )
        with self.assertRaises(ValidationError):
            response.full_clean()

    def test_response_email_must_be_valid(self):
        response = Response.objects.create(
            name='Foo',
            email='not an email',
            message='Foo message'
        )
        with self.assertRaises(ValidationError):
            response.full_clean()

    def test_response_message_is_required(self):
        response = Response.objects.create(
            name='Foo',
            email='foo@example.com',
        )
        with self.assertRaises(ValidationError):
            response.full_clean()
