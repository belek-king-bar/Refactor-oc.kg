from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse
import json

class AddToFavoritesTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/bookmarks', verbosity=0)
        self.client = Client()

    def test_details(self):
        response = self.client.post(reverse('webapp:from_favorites'),
                                    {'movie_id': 6, 'user_pk': 1})
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.content)
        print(response)
        self.assertEqual(type(response), list)
        self.assertTrue('movie' in response[0])
