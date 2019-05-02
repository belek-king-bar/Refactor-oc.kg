import sys
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cinema2',
        'USER': 'root',
        'PASSWORD': '7325real2342',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

if 'test' in sys.argv:
    DATABASES = {
        'default': {'ENGINE': 'django.db.backends.sqlite3'}
    }
