# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'PORT': 5433,
        'NAME': "qingdaooj",
        'USER': "qingdaooj",
        'PASSWORD': 'qingdaooj'
    }
}

REDIS_CONF = {
    "host": "127.0.0.1",
    "port": "6379"
}


DEBUG = True

ALLOWED_HOSTS = ["*"]

DATA_DIR = f"{BASE_DIR}/data"
