# -*- coding: utf-8 -*-
from .jsobject import Object  # noqa
from .encoder import dump, dumps  # noqa
from .decoder import load, loads  # noqa
from .convert import convert  # noqa
import os

HERE = os.path.abspath(os.path.dirname(__file__))

__author__ = 'Marcin Wierzbanowski'
__version__ = '0.10.2'
# open(os.path.join(HERE, '..', 'VERSION')).read()[:-1]
__license__ = 'MIT'

"""
JsObject is simple implementation JavaScript-Style Objects in Python.

Homepage and documentation: http://mavier.github.io/jsobject.

Copyright (c) 2014, Marcin Wierzbanowski.
License: MIT (see LICENSE for details)
"""
