import os
import sys
from distutils.util import strtobool
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from django.urls import reverse_lazy

from .google_cloud import apply_datastore_env_vars, setup_cloud_logging

GOOGLE_CLOUD_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT')

if GOOGLE_CLOUD_PROJECT:
    apply_datastore_env_vars(GOOGLE_CLOUD_PROJECT)

try:
    DEBUG = bool(strtobool(os.environ.get('DJANGO_DEBUG', '')))
except ValueError:
    DEBUG = False

TEST = 'test' in sys.argv

if not DEBUG:
    setup_cloud_logging()

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
]

BASE_DIR = Path(__file__).resolve().parent.parent

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
    'cspreports',
    'blog',
    'contact',
    'healthcheck',
    'pages',
    'projects',
]

MIDDLEWARE = [
    'liamnewmarch.middleware.CanonicalHostRedirectMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
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

CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SAMESITE = 'Strict'

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = 10

    SECURE_REDIRECT_EXEMPT = [r'^healthcheck/$']
    SECURE_REFERRER_POLICY = 'same-origin'

    SECURE_SSL_REDIRECT = True


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
                'liamnewmarch.context_processors.globals',
            ],
        },
    },
]


# Database

if TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'gcloudc.db.backends.datastore',
            'INDEXES_FILE': str(BASE_DIR / 'djangaeidx.yaml'),
            'PROJECT': 'liamnewmarch-blog',
        },
    }

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
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

ADMIN_NAME = os.environ.get('ADMIN_NAME')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

if ADMIN_NAME and ADMIN_EMAIL:
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]
    DEFAULT_FROM_EMAIL = SERVER_EMAIL = f'{ADMIN_NAME} <{ADMIN_EMAIL}>'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = 'apikey'
    EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


# CSP

CSP_BLOCK_ALL_MIXED_CONTENT = True
CSP_DEFAULT_SRC = ()
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com',)
CSP_IMG_SRC = ("'self'", 'https:',)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com',)

CSP_REPORTS_EMAIL_ADMINS = False
CSP_REPORTS_LOG_LEVEL = 'error'
CSP_REPORTS_SAVE = False

STACKDRIVER_API_KEY = os.environ.get('STACKDRIVER_API_KEY')

if DEBUG:
    # Browsersync
    CSP_CONNECT_SRC = ("'self'",)
    CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'",)
else:
    # Enable nonces for script elements
    CSP_INCLUDE_NONCE_IN = ('script-src',)
    CSP_REPORT_URI = reverse_lazy('report_csp')
