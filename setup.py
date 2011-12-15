#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='django-statsd-toolbar',
      version='0.1.1',
      description='statsd debug panel for djang-debug-toolbar',
      author='Mike Ryan',
      author_email='mike@fadedink.co.uk',
      url='https://github.com/mikery/statsd-debug-toolbar',
      packages=['statsd_toolbar'],
      package_data = {'statsd_toolbar': ['templates/panels/*',
                                         'panels/*']}
)
