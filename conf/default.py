#-*- coding: utf-8 -*-

import os

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
location = lambda *path: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', *path)
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    location('static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#w%yp9_5wnupojr=4o0mwap#!)y=q9ovu=o#xnytga7u5^bf27'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    location('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SUIT_CONFIG = {
    'ADMIN_NAME': 'haveyouheard'
}

# Application definition
INSTALLED_APPS = (
    'suit',  # Pretty admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',

    # Rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',

    # Other 3rd party
    'mailchimp',
    'djmoney',
    'corsheaders',

    # haveyouheard
    'apps.common',
    'apps.users',
    'apps.events',
    'apps.tickets',
    'apps.experiments',
    'apps.notifications',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'PAGINATE_BY': 20,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
}

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'users.User'

## Currency
import moneyed
from moneyed.localization import _FORMATTER, DEFAULT

DEFAULT_CURRENCY_CODE = 'GBP'
GBP_CHOICE_TUPLE = [(DEFAULT_CURRENCY_CODE, "Pound Sterling")]

_FORMATTER.add_sign_definition(DEFAULT, moneyed.GBP, prefix=u"£")
_FORMATTER.add_sign_definition(DEFAULT, moneyed.USD, prefix=u"$")
_FORMATTER.add_sign_definition(DEFAULT, moneyed.AUD, prefix=u"A$")
_FORMATTER.add_sign_definition(DEFAULT, moneyed.EUR, prefix=u"€")

CURRENCIES = [
    'GBP',
    'USD',
    'AUD',
    'EUR',
]

CURRENCY_CHOICES = [
    (DEFAULT_CURRENCY_CODE, moneyed.get_currency(DEFAULT_CURRENCY_CODE).name),
]

# API SETTINGS AND CREDENTIALS
#--------------------------------------------------------

# Production key, but test list.
MAILCHIMP_API_KEY = '2e175c4f1d007c9a1750e2d7993eb626-us10'
MAILCHIMP_MAIN_LIST_ID = '075d485454'

TICKET_EVOLUTION_TOKEN = 'bdb802b503ff68f0072b95f35f3f2fa5'
TICKET_EVOLUTION_SECRET = 'efDpKWr6yeUH20FnMLgY5IHdKpteoK+g4UzCgDRr'
TICKET_EVOLUTION_USE_SANDBOX = True
TICKET_EVOLUTION_URL_PREFIX = '/v9'

STUBHUB_APPLICATION_TOKEN = 'FR_EAm_IXA_vHtromlp6200jQvIa'
STUBHUB_URL = 'https://10.80.81.177:8243'
