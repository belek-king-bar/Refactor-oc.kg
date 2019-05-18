from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, login, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")
        if not login:
            raise ValueError("I KNOW YOU HAVE A NAME")
        user = self.model(
            email=self.normalize_email(email),
            login=login,
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, login, **extra_fields):
        user = self.create_user(email, password, login, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user
