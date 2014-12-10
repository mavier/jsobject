#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JsObject is simple implementation JavaScript-Style Objects in Python.

Homepage and documentation: http://mavier.github.io/jsobject.

Copyright (c) 2014, Marcin Wierzbanowski.
License: MIT (see LICENSE for details)
"""
from __future__ import with_statement
import os
HERE = os.path.abspath(os.path.dirname(__file__))

__author__ = 'Marcin Wierzbanowski'
__version__ = open(os.path.join(HERE, '..', 'VERSION')).read()[:-1]
__license__ = 'MIT'


class Object(object):
    """ This is a base class """

    def __init__(self, data={}):
        if type(data) not in (dict, Object):
            raise TypeError("argument must be dict, not %s"
                            % type(data).__name__)

        for k, v in self.__get(data).items():
            self.__dict__[k] = self.__set(v)

    def __setattr__(self, k, v):
        self.__dict__[k] = Object(v) if type(v) == dict else v

    def get(self):
            return dict((k, self.__get(v)) for (k, v) in self.__dict__.items())

    def __get(self, v):
        return v.get() if type(v) == Object else v

    def __set(self, v):
        return Object(v) if type(v) == dict else v

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())

    def __eq__(self, other):
        return str(self) == str(other)

    def __contains__(self, k):
        return k in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, k):
        return self.__dict__[k]

    def __setitem__(self, k, v):
        self.__dict__[k] = Object(v) if type(v) == dict else v
