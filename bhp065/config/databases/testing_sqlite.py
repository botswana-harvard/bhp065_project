# import os

TESTING_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_name.sqlite',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'lab_api': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lab',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'destination': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'macair',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'dispatch_destination': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'producer',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
}
