# -*- coding: utf-8 -*-

from jsobject import Object
import unittest

"""Tests for jsobject created from python dict"""

class JsobjectPyobjectTestcase(unittest.TestCase):

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
        self.js = Object(self.data)

    def tearDown(self):
        pass

    def test_len(self):
        assert len(self.js) == len(self.data)

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

    def test_get_object_g(self):
        assert self.js.objectA.g == self.data['objectA']['g']

    def test_get_object_h(self):
        assert self.js.objectA.g.h == self.data['objectA']['g']['h']

    def test_object_contain(self):
        assert "objectA" in self.js

    def test_set_get(self):
        self.js.__setattr__("test", "TEST")
        assert self.js.__getitem__('test') == "TEST"

