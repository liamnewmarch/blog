import json

from django.test import TestCase


class HealthcheckTestCase(TestCase):
    def test_healthcheck_endpoint(self):
        response = self.client.get('/healthcheck/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIsInstance(content, dict)
        self.assertEqual(content['status'], 'success')
        self.assertTrue('timestamp' in content)
