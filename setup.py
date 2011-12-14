#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='django-statsd-toolbar',
      version='0.1.0',
      description='statsd debug panel for djang-debug-toolbar',
      author='Mike Ryan',
      author_email='mike@fadedink.co.uk',
      url='https://github.com/mikery/statsd-debug-toolbar',
      packages=['statsd_toolbar'],
      requires=['django (>=1.2)']
)
