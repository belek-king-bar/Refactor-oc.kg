from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class BestsellerViewTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/bestsellers', verbosity=0)
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('webapp:bestseller_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['movie_all']), 10)
        self.assertEqual(type(response.context['movie_all']), list)
        for i in response.context['movie_all']:
            self.assertEqual(type(i), dict)
        self.assertEqual(type(response.context['movie_all'][0]['category']), str)
        self.assertEqual(type(response.context['movie_all'][0]['movies']), list)

