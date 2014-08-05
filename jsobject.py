#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Jsobject is simple implementation JavaScript-Style Objects in Python.

Homepage and documentation: http://mavier.github.io/jsobject.

Copyright (c) 2014, Marcin Wierzbanowski.
License: MIT (see LICENSE for details)
"""

from __future__ import with_statement

__author__ = 'Marcin Wierzbanowski'
__version__ = '0.0.1-dev'
__license__ = 'MIT'

try: from simplejson import dumps, loads
except ImportError:
    try: from json import dumps, loads
    except ImportError:
        try: from django.utils.simplejson import dumps, loads
        except ImportError:
            def dumps(data):
                raise ImportError("JSON support requires Python 2.6 or simplejson.")
            loads = dumps

class jsobject(object):
    _locked = False
    def __init__(self, data):
        self._current = {}
        self._current2 = {}
        self._path = self.__class__.__name__
        self.loads(data)
        pass

    def loads(self, data):
        self._data = data

    def data(self):
        return self._data

    def __getattr__(self, name):
            # print "-----> GET:", name
            if name[0] == "_":
                return self.__dict__[name]
            # print "2->", name, self._current
            if self._current == {}:
                self._current = self._data
            if name in self._current:
                if type(self._current[name]) == dict:
                    self._current = self._current[name]
                    self._current2 = self._current
                    self._path += ".%s" % name
                    return self
                else:
                    value = self._current[name]
                    self._current = {}
                    self._path = self.__class__.__name__
                    return value
            else:
                path = self._path + "." + name
                self._current = {}
                self._path = self.__class__.__name__
                raise AttributeError('object has no attribut ' + path)

    def __setattr__(self, name, value):
        # print "->", str(name)
        if name[0]=="_":
            self.__dict__[name] = value
            return
        if self._current2 == {}:
            self._current2 = self._data
        if name in self._current2:
            if type(self._current2[name]) == dict:
                print "dict"
                self._current2 = self._current2[name]
            else:
                print "nodict"
                self._current2[name] = value
        else:
            print "n:", name, self._current2
            # print self._current2
            self._current2[name] = value
            self._current2 = {}

def __str__(self):
    output = str(self._current)
    self._current = {}
    return output

# THE END
