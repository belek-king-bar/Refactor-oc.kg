from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse
import json

class CommentAddTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        self.client = Client()

    def test_details(self):
        response = self.client.post(reverse('webapp:add_comment'),
                                    {'movie_id': 4, 'text': 'Плохой фильм', 'user_pk': 1})
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.content)
        self.assertEqual(type(response), list)
        self.assertTrue('user' in response[0])
        self.assertTrue('text' in response[0])
        self.assertTrue('created_at' in response[0])
