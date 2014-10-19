#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JsObject is simple implementation JavaScript-Style Objects in Python.

Homepage and documentation: http://mavier.github.io/jsobject.

Copyright (c) 2014, Marcin Wierzbanowski.
License: MIT (see LICENSE for details)
"""

from __future__ import with_statement

__author__ = 'Marcin Wierzbanowski'
__version__ = '0.9.0'
__license__ = 'MIT'

class JsObject(object):
    def __init__(self, data):
        for k, v in self.__get(data).iteritems():
            self.__dict__[k] = self.__set(v)

    def __setattr__(self, k, v):
        self.__dict__[k] = JsObject(v) if type(v) == dict else v

    def __dump(self):
        return {k: self.__get(v) for k, v in self.__dict__.iteritems()}

    def __get(self, v):
        return v.__dump() if type(v) == JsObject else v

    def __set(self, v):
        return JsObject(v) if type(v) == dict else v

    def __str__(self):
        return str(self.__dump())

    def __repr__(self):
        return str(self.__dump())

    def __eq__(self, other):
        return str(self) == str(other)

    def __contains__(self, k):
        return k in self.__dict__

    def __len__(self):
        return len(self.__dict__)

if __name__ == "__main__":

    def d(data):
        print dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

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

    js = JsObject(data)
    js2 = JsObject(js)

    js.name = 5
    js.nameDict = {}
    js.nameDict2 = {"objectB": "b"}
    js.nameDict3 = {"objectC": {"a": "A", "b":"B"}}

    print js.name == 5
    print js.nameDict
    print js.nameDict2
    print js.nameDict3
    print js.nameDict3.objectC
    print js.nameDict3.objectC.a
    print "--"
    print type(js.nameDict)
    print type(js.nameDict2)
    print type(js.nameDict3)
    print type(js.nameDict3.objectC)
    print "--"
    print js

    print js.string == data['string']
    print js.number == data['number']
    print js.null == data['null']
    print js.boolean == data['boolean']
    print js.array == data['array']
    print js.objectA != data['objectA']
    print js.objectA
    print data['objectA']
    print js.objectA.a == data['objectA']['a']
    print js.objectA.c == data['objectA']['c']
    print js.objectA.g == data['objectA']['g']
    print js.objectA.g.h == data['objectA']['g']['h']
    print "string" in js
    print len(js)

    c = JsObject(data)

    print "--- 0 ------"
    print c.string
    print c.objectA

    print "set -- 0 ------"
    c.string = "str2"
    c.objectA.g.h = "BBB"

    print "--- 1 ------"
    print c.string
    print c.objectA.g.h
    print c.objectA


    print "--- 2 ------"
    print c.string
    print c.objectA

    print "--- 3 ------"
    print c.number
    print c.objectA.a

    print c.number
    print c.objectA.e

    print "--- 4 ------"
    try:
        print c.objectA.e2
    except BaseException:
        print "err e2"

    print "--- 5 ------"

    c.string = "str4"
    print c.string

    c.objectA.e = "ccc"
    print c.objectA.e

    print "--- 6------"
    print c.objectA.g.h

    print "--- 7------"
    c.objectA = {"a": "AAA"}
    print c.objectA

    print "--- 8 ------"
    c.string = "str2"
    print c.string

    print "--- 9 ------"
    c.objectB = {}
    print c.objectB

    c.objectB = {"a": {"c": "CCC"}}
    print c.objectB

    print "---- 10 -----"
    c.objectB.a.c = "BBB"
    print c.objectB.a.c

    print "---- 11 -----"
