# -*- coding: utf-8 -*-

import unittest
import pytest
from jsobject import Object

"""Tests for jsobject created from python dict"""


class ObjectTestcase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.data = {
            "array": [1, 2, 3],
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
                    },
                },
            "string": "Hello World",
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

    def test_get_key(self):
        assert self.js['objectA'] == self.data['objectA']

    def test_object_contain(self):
        assert "objectA" in self.js

    def test_set_get(self):
        self.js.__setattr__("test", "TEST")
        assert self.js.__getitem__('test') == "TEST"

    def test_create_empty(self):
        Object()

    def test_create_object(self):
        Object(self.js)

    def test_array_element(self):
        assert self.js.array[0] == self.data['array'][0]

    def test_set_string(self):
        self.js.string = "string"

    def test_set_number(self):
        self.js.number = 321

    def test_set_null(self):
        self.js.null = None

    def test_set_boolean(self):
        self.js.boolean = False

    def test_set_array(self):
        self.js.array = [4, 5, 6]

    def test_set_key(self):
        self.js['objectA'] = {"a": "A"}
        assert self.js.objectA.a == "A"

    def test_set_object(self):
        self.js.objectA = {"a": "A"}

    def test_set_object_a(self):
        self.js.objectA.a = "A"

    def test_set_object_b(self):
        self.js.objectA.c = {}

    def test_set_object_g(self):
        self.js.objectA.g = {"h": {"i": "I"}}

    def test_set_object_h(self):
        self.js.objectA.g.h = {"j": "J"}

    def test_create_list(self):
        with pytest.raises(TypeError):
            Object([1, 2, 3])

    def test_get_not_exist(self):
        with pytest.raises(AttributeError):
            self.js.objectA.e2

    def test_dump(self):
        import json
        json.dumps(self.js.get(), sort_keys=True,
                   indent=4, separators=(',', ': '))
