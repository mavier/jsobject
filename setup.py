#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import multiprocessing

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.version_info < (2, 6):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python \
                               3.x to use jsobject.")

HERE = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(HERE, 'README.rst')).read()

if not os.path.exists('VERSION'):
    os.system("git describe --tags | cut -c 2- > VERSION")

version = open(os.path.join(HERE, 'VERSION')).read()[:-1]

setup(
    name='jsobject',
    version=version,
    description='Jsobject is simple implementation JavaScript-Style Objects \
                 in Python.',
    long_description=readme,
    author='Marcin Wierzbanowski',
    author_email='marcin@wierzbanowski.com',
    url='http://mavier.github.io/jsobject',
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    data_files=['VERSION'],
    license='MIT',
    platforms='any',
    keywords=['jsobject', 'Object', 'json', 'chain', 'javascript'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
