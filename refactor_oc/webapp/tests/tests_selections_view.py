from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class SelectionViewTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/selections', verbosity=0)
        self.client = Client()


    def test_details(self):
        response = self.client.get(reverse('webapp:selection_list'))
        self.assertEqual(response.status_code, 200)
