from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class SelectionDetailViewTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/selections', verbosity=0)
        self.client = Client()

    def test_get_selection_detail(self):
        response = self.client.get(reverse('webapp:selection_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

