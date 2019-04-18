from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cinema2',
        'USER': 'root',
        'PASSWORD': 'madness322',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
