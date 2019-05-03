from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class CatalogueViewTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/auth_user', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/user', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)

        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('webapp:catalogue_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('movie_list' in response.context)
        self.assertTrue('movies' in response.context)
        self.assertTrue('comments' in response.context)
        self.assertTrue('page' in response.context)
        self.assertEqual(len(response.context['comments']), 5)
