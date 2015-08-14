# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bhp065_project',
    version='0.1.0dev0',
    author=u'mrbkew',
    author_email='mrbkew@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://github/botswana-harvard/bhp065_project',
    license='GPL license, see LICENSE',
    description='bhp065_project',
    long_description=README,
    zip_safe=False,
    keywords='django ledc bhp065',
    install_requires=[
        'Django==1.6.11',
        'django-extensions>=1.5.5',
        'unipath>=1.1',
        'python-dateutil>=2.4.2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
