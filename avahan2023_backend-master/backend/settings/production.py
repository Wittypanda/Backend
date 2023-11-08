from .base import *
from decouple import config

APP_URL = "https://avahan-portal.vercel.app"
HOST_URL = "https://avahan24.live/"

DEBUG = False

ALLOWED_HOSTS = [
    'avahan24.live', 'www.avahan24.live','localhost']

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
    'https://avahan24.live',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vcet.sports@vcet.edu.in'
EMAIL_HOST_PASSWORD = 'qvhjgjfoyzmzqogj'

