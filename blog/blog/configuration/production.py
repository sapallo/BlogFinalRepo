import os
from .base import * 

DEBUG = False 

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'production-domain.com']

DATABASES = {
    'default': {
        # En caso de usar postgresql
        # 'ENGINE': 'django.db.backends.postgresql
        # En caso de usar mysql
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'), # valor de la variable de entorno DB_NAME en el .env
        'USER': os.getenv('DB_USER'), # valor de la variable de entorno DB_USER en el .env
        'PASSWORD': os.getenv('DB_PASSWORD'), # valor de la variable de entorno DB_PASSWORD en el .env
        'HOST': os.getenv('DB_HOST'), # valor de la variable de entorno DB_HOST en el .env
        'PORT': os.getenv('DB_PORT'), # valor de la variable de entorno DB_PORT en el .env
    }
}

os.environ['DJANGO_PORT'] = '8080'
