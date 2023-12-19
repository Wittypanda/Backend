from .base import *
from decouple import config

APP_URL = "https://avahan-portal.vercel.app"
HOST_URL = "https://avahan24.live/"

DEBUG = False

ALLOWED_HOSTS = ['134.209.154.26','10.122.0.2','avahan24.live', 'www.avahan24.live','localhost','127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'avahan_2024',
        'USER': 'avahan_user',
        'PASSWORD': 'avahan',
        'HOST': 'localhost',
    }
}

CORS_ALLOWED_ORIGINS = [
    'https://avahan24.live', 'https://avahan-portal.vercel.app/' , 'https://localhost:3000'
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vcet.sports@vcet.edu.in'
EMAIL_HOST_PASSWORD = 'qvhjgjfoyzmzqogj'

