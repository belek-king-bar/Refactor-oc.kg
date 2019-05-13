from webapp.models import OCUser
from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command
from django.conf import settings
from webauth.forms import OCUserCreationForm


class TestUserSignUpForm(TestCase):
    def test_registration_form(self):
        invalid_data = {
            "login": "name",
            "email": "name@name.com",
            "password1": "1qaz@WSX29",
            "password2": "not1qaz@WSX29"
        }
        form = OCUserCreationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        valid_data = {
            "login": "name",
            "email": "name@name.com",
            "password1": "1qaz@WSX29",
            "password2": "1qaz@WSX29"
        }
        form = OCUserCreationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)


class TestUserSignUpView(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/users', verbosity=0)
        self.client = Client()

    def test_registration_view_initial(self):
        response = self.client.get(reverse('webauth:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'registration/signup.html')
        self.failUnless(isinstance(response.context['form'],
                                   OCUserCreationForm))

    def test_registration_view_success(self):
        users = OCUser.objects.count()
        valid_data = {
            "login": "name",
            "email": "name@name.com",
            "password1": "1qaz@WSX29",
            "password2": "1qaz@WSX29"
        }
        response = self.client.post(reverse('webauth:signup'), valid_data)
        self.assertEqual(response.status_code, 302)
        new_users = OCUser.objects.count()
        self.assertGreater(new_users, users)

    def test_registration_view_failure(self):
        invalid_data = {
            "login": "name",
            "email": "name@name.com",
            "password1": "1qaz@WSX29",
            "password2": "not1qaz@WSX29"
        }
        response = self.client.post(reverse('webauth:signup'), invalid_data)
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field='password2',
                             errors=u"Два поля с паролями не совпадают.")

