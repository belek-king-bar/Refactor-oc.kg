from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from webapp.models import OCUser


class OCUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = OCUser
        fields = ('login', 'email')


class OCUserChangeForm(UserChangeForm):

    class Meta:
        model = OCUser
        fields = ('login', 'email')

