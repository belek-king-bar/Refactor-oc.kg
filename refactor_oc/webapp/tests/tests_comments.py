from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse

class CommentsTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('webapp:movie_comments', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('movie' in response.context)
        self.assertTrue('comments' in response.context)
