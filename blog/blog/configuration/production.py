import os
from .base import * 
DEBUG = False 

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'production-domain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

os.environ['DJANGO_PORT'] = '8080'
