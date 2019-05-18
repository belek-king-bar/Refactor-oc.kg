from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse

class MovieDetailTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/ratings', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/roles', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/persons', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/participants', verbosity=0)
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('webapp:movie_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('movie' in response.context)
        self.assertEqual(type(response.context['comments_len']), int)
        self.assertTrue('compilation' in response.context)
        self.assertTrue('actors' in response.context)
        self.assertTrue('producers' in response.context)
        self.assertEqual(len(response.context['compilation']), 5)
        self.assertEqual(response.context['compilation'].model.__name__, 'Movie')