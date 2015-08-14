# import os

TESTING_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/django/source/bhp065_project/bhp065.sqlite',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'cancer': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'lab_api': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/django/source/bhp065_project/lab',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'destination': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/django/source/bhp065_project/macair',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'dispatch_destination': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/django/source/bhp065_project/producer',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
}
