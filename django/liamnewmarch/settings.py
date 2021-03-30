import os
from distutils.util import strtobool
from pathlib import Path

from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
]

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    DEBUG = bool(strtobool(os.environ.get('DJANGO_DEBUG', '')))
except ValueError:
    DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())


# Application

INSTALLED_APPS = [
    'gcloudc',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'blog',
    'pages',
    'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

ROOT_URLCONF = 'liamnewmarch.urls'

WSGI_APPLICATION = 'liamnewmarch.wsgi.application'


# Security

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'django.contrib.auth.password_validation.{validator}'
    } for validator in (
        'UserAttributeSimilarityValidator',
        'MinimumLengthValidator',
        'CommonPasswordValidator',
        'NumericPasswordValidator',
    )
]

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 10
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = 'same-origin'
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True


# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'liamnewmarch.context.globals',
            ],
        },
    },
]


# Database

DATABASES = {
    'default': {
        'ENGINE': 'gcloudc.db.backends.datastore',
        'INDEXES_FILE': str(BASE_DIR / 'djangaeidx.yaml'),
        'PROJECT': 'liamnewmarch-blog',
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


# Internationalisation

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'


# Email

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
