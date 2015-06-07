#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.version_info < (2, 6):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python \
                               3.x to use jsobject.")

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


HERE = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(HERE, 'README.rst')).read()

# if not os.path.exists('VERSION'):
#     os.system("git describe --tags | cut -c 2- > VERSION")

version = '0.10.2'
# open(os.path.join(HERE, 'VERSION')).read()[:-1]

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
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    license='MIT',
    platforms='any',
    keywords=['jsobject', 'Object', 'json', 'chain', 'javascript'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
