import os
import sys
import socket

from unipath import Path

from config.installed_apps import DJANGO_APPS, THIRD_PARTY_APPS, EDC_APPS, LIS_APPS, LOCAL_APPS
from config.databases import TESTING_SQLITE

DEBUG = True
TEMPLATE_DEBUG = DEBUG

APP_NAME = 'hnscc'
PROJECT_NUMBER = 'BHP065'
PROJECT_IDENTIFIER_PREFIX = '065'

# PATHS
DIRNAME = os.path.dirname(os.path.abspath(__file__))
SOURCE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(3)
EDC_DIR = SOURCE_ROOT.child('edc_project').child('edc')
TEMPLATE_DIRS = (
    EDC_DIR.child('templates'),
)
PROJECT_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2)
PROJECT_DIR = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)
APP_DIR = PROJECT_DIR.child('apps').child(APP_NAME)
ETC_DIR = PROJECT_DIR.child('config').child('etc')
MEDIA_ROOT = PROJECT_DIR.child('media')
STATIC_ROOT = PROJECT_DIR.child('static')
FIXTURE_DIRS = (
    APP_DIR.child('fixtures'),
)
STATICFILES_DIRS = ()
CONFIG_DIR = PROJECT_DIR.child('config')
MAP_DIR = STATIC_ROOT.child('img')

KEY_PATH = PROJECT_DIR.child('keys')

# DATABASES
DATABASES = TESTING_SQLITE
CONN_MAX_AGE = 15
testing_db_name = 'sqlite'


ALLOWED_HOSTS = ['localhost']

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

LANGUAGE_CODE = 'en'

SITE_ID = 1
SITE_CODE = '040'

MEDIA_URL = '/media/'


STATIC_URL = '/static/'

STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '12345'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
     'django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
     )),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages",
                               )

ROOT_URLCONF = 'config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + EDC_APPS + LIS_APPS + LOCAL_APPS

# django
SESSION_COOKIE_AGE = 10000
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# django auth
AUTH_PROFILE_MODULE = "bhp_userprofile.userprofile"

# admin overrides
LOGIN_URL = '/{app_name}/login/'.format(app_name=APP_NAME)
LOGIN_REDIRECT_URL = '/{app_name}/'.format(app_name=APP_NAME)
LOGOUT_URL = '/{app_name}/logout/'.format(app_name=APP_NAME)

# south
SOUTH_LOGGING_FILE = os.path.join(os.path.dirname(__file__), "south.log")
SOUTH_LOGGING_ON = True

# dajax
DAJAXICE_MEDIA_PREFIX = "dajaxice"

ALLOW_MODEL_SERIALIZATION = False

DEVICE_ID = '95'
SERVER_DEVICE_ID_LIST = []
MIDDLEMAN_DEVICE_ID_LIST = []
FIELD_MAX_LENGTH = 'migration'
IS_SECURE_DEVICE = True

SUBJECT_TYPES = ['subject', ]
MAX_SUBJECTS = {'subject': 300, }
SUBJECT_APP_LIST = ['hnscc_subject', ]
DISPATCH_APP_LABELS = []

PROJECT_TITLE = 'TEST: Head & Neck Squamous Cell Carcinoma'
INSTITUTION = 'Botswana-Harvard AIDS Institute Partnership'
PROTOCOL_REVISION = 'V1.0 XX May 20XX'
