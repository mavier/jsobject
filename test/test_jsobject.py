#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from jsobject import jsobject as JS

"""Tests for jsobject created from python dict"""

class JsobjectPyObjectTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.data = {
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

        self.js = JS(self.data)

    def tearDown(self):
        pass

    def test_get_string(self):
        assert self.js.string == self.data['string']

    def test_get_number(self):
        assert self.js.number == self.data['number']

    def test_get_null(self):
        assert self.js.null == self.data['null']

    def test_get_boolean(self):
        assert self.js.boolean == self.data['boolean']

    def test_get_array(self):
        assert self.js.array == self.data['array']

    def test_get_object(self):
        assert self.js.objectA == self.data['objectA']

    def test_get_object_a(self):
        assert self.js.objectA.a == self.data['objectA']['a']

    def test_get_object_b(self):
        assert self.js.objectA.c == self.data['objectA']['c']

