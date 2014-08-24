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
__version__ = '0.0.2-dev'
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

    def __str__(self):
        value = str(self._current)
        self._current = {}
        self._current2 = {}
        return value

    def __getattr__(self, name):
        # print "1-> GET:", name
        if name[0] == "_":
            return self.__dict__[name]
        print "2->", name, self._current
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
            value = self._current
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
                # print "dict"
                self._current2 = self._current2[name]
            else:
                # print "nodict"
                self._current2[name] = value
        else:
            # print "n:", name, self._current2
            # print self._current2
            self._current2[name] = value
            self._current2 = {}

def __str__(self):
    output = str(self._current)
    self._current = {}
    return output

# THE END

if __name__ == "__main__":
    data = {
      "array": [
        1,
        2,
        3
      ],
      "boolean": True,
      "null": None,
      "number": 123,
      "objectA": {
        "a": "b",
        "c": "d",
        "e": "f",
        "g": {
            "h": "i",
            "j": {
                "k": "l"
                }
            }
      },
      "string": "Hello World"
    }

    def dump(c):
        print "---------"
        print "c1:", c._current
        print "c2:", c._current2
        print "---------"
        print c._data
        print "---------"

    c = jsobject(data)

    print "--- 0 ------"
    print c.string
    print c.objectA

    print "--- 1 ------"
    print c.string
    print c.objectA

    print "--- 2 ------"
    print c.string
    print c.objectA

    print "--- 3 ------"
    print c.number
    print c.objectA.a

    print c.number
    print c.objectA.e
    try:
        print c.objectA.e2
    except:
        print "err e2"
        pass

    print c.objectA
    print c.number

    print "--- 4 ------"

    c.string = "str2"
    c.objectA.g.h = "BBB"

    dump(c)

    print c.objectA.g.h

    dump(c)

    # c.objectA = {"a": "AAA"}
    # print c.objectA

    # print "--- 5 ------"
    #
    # c.string = "str2"
    # c.objectB = {}
    # c.objectB = {"a": "AAA"}
    # print "---------"
    # print c.objectB
    # c.objectB.a.c = "BBB"
    # print c.data()
