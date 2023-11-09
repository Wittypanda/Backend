from .base import *
from decouple import config

APP_URL = "http://localhost:3000"
HOST_URL = "http://127.0.0.1:8000"

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '143.244.136.17', '10.122.0.2',
                 'avahan24.live', 'www.avahan24.live',
                 'eventapp.avahan24.live', 'www.eventapp.avahan24.live']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# Email Credentials
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ' vcet.sports@vcet.edu.in'
EMAIL_HOST_PASSWORD = 'qvhjgjfoyzmzqogj'
