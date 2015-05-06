# -*- coding: utf-8 -*-

import unittest
import pytest
from jsobject import Object, loads, dumps


class ObjectTestcase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.data = {
            "array": [1, 2, 3],
            "someitems": [
                "str",
                1,
                ["s1", 2, {"s2": "S2"}],
                {"node": "a"}
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
                    },
                },
            "string": "Hello World",
            }

        data = dumps(self.data)
        self.js = loads(data)

    def tearDown(self):
        pass

    def test_set_jsobject(self):
        obj = loads('{"a":"A", "b":{"c":"C"}}')
        self.js.objectA.a = obj 
        assert self.js.objectA.a.b == {"c": "C"}


