#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2,5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use jsobject.")

import jsobject
HERE = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(HERE, 'README.rst')).read()

setup(
    name             = 'jsobject',
    version          = jsobject.__version__,
    description      = 'Jsobject is simple implementation JavaScript-Style Objects in Python.',
    long_description = readme,
    author           = 'Marcin Wierzbanowski',
    author_email     = 'marcin@wierzbanowski.com',
    url              = 'http://mavier.github.io/jsobject',
    py_modules       = ['jsobject'],
    scripts          = ['jsobject.py'],
    license          = 'MIT',
    platforms        = 'any',
    keywords         = ['jsobject', 'JsObject', 'json', 'chain', 'javascript', 'object'],
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
