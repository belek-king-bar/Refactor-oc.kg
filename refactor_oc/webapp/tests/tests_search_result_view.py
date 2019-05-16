from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class SearchViewTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/comments', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/genres', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/movies', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/persons', verbosity=0)
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('webapp:search_list'), {'q': 'Тачки'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('movies' in response.context)
        self.assertTrue('persons' in response.context)
        self.assertTrue(len(response.context['movies']) <= 6)
        self.assertTrue(len(response.context['persons']) <= 6)
        for i in response.context['persons']:
            self.assertEqual(type(i.name), str)
            self.assertEqual(type(i.international_name), str)
        for i in response.context['movies']:
            self.assertEqual(type(i.name), str)
            self.assertEqual(type(i.international_name), str)
