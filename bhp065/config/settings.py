import os
import sys
import socket

from unipath import Path

from bhp065.config.installed_apps import DJANGO_APPS, THIRD_PARTY_APPS, EDC_APPS, LIS_APPS, LOCAL_APPS
from bhp065.config.databases import TESTING_SQLITE

DEBUG = True  # Note: should be False for collectstatic
TEMPLATE_DEBUG = DEBUG
# ADMINS = ('',)

APP_NAME = 'hnscc'

# PATHS
DIRNAME = os.path.dirname(os.path.abspath(__file__))  # needed??
SOURCE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(3)  # e.g. /home/django/source
EDC_DIR = SOURCE_ROOT.child('edc_project').child('edc')  # e.g. /home/django/source/edc_project/edc
TEMPLATE_DIRS = (
    EDC_DIR.child('templates'),
)
PROJECT_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2)  # e.g. /home/django/source/bhp066_project
PROJECT_DIR = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)  # e.g. /home/django/source/bhp066_project/bhp066
APP_DIR = PROJECT_DIR.child('apps').child(APP_NAME)  # e.g. /home/django/source/bhp066_project/bhp066/apps/bcpp
ETC_DIR = PROJECT_DIR.child('config').child('etc')  # for production this should be /etc/edc
MEDIA_ROOT = PROJECT_DIR.child('media')
STATIC_ROOT = PROJECT_DIR.child('static')
FIXTURE_DIRS = (
    APP_DIR.child('fixtures'),
)
STATICFILES_DIRS = ()
CONFIG_DIR = PROJECT_DIR.child('config')
MAP_DIR = STATIC_ROOT.child('img')

# edc.crytpo_fields encryption keys
KEY_PATH = PROJECT_DIR.child('keys')

# DATABASES
DATABASES = TESTING_SQLITE
CONN_MAX_AGE = 15
testing_db_name = 'sqlite'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', 'bhpserver']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Gaborone'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# langauage setting

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

LANGUAGE_CODE = 'en'

SITE_ID = 1

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL that handles the static files served from STATIC_ROOT.
STATIC_URL = '/static/'

# A list of locations of additional static files
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

SERVER_DEVICE_ID_LIST = []
MIDDLEMAN_DEVICE_ID_LIST = []
FIELD_MAX_LENGTH = 'migration'
IS_SECURE_DEVICE = True
MAX_SUBJECTS = 3000