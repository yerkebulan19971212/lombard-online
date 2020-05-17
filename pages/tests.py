from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reversed('home'))
        self.assertEqual(response.status_code, 200)
