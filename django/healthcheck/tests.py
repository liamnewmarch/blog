from django.test import TestCase


class HealthcheckTestCase(TestCase):
    def test_healthcheck_endpoint(self):
        response = self.client.get('/healthcheck/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b'')
