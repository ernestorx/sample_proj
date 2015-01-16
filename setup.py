#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import 
version = .__version__

setup(
    name='project_name is the title of the project.',
    version=version,
    author='',
    author_email='ernesto@tryolabs.com',
    packages=[
        '',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['/manage.py'],
)
