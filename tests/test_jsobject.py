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

    def test_get_key(self):
        assert self.js['objectA'] == self.data['objectA']

    def test_object_contain(self):
        assert "objectA" in self.js

    def test_create_empty(self):
        Object()

    def test_create_object(self):
        Object(self.data)

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

    def test_set_object(self):
        self.js.objectA = {"a": "A"}

    def test_set_key(self):
        self.js['objectA'] = Object({"a": "A"})
        assert self.js.objectA.a == "A"

    def test_create_list(self):
        with pytest.raises(TypeError):
            Object([1, 2, 3])

    def test_get_not_exist(self):
        with pytest.raises(KeyError):
            self.js.objectA.e2

    def test_get_from_list_str(self):
        self.js.someitems[0] == "str"

    def test_get_from_list_list(self):
        self.js.someitems[2][0] == "s1"
        self.js.someitems[2][1] == 2

    def test_get_from_list_dict(self):
        self.js.someitems[3].node == "a"

    def test_dict_dict(self):
        assert isinstance(Object({"a":"A"}), dict)


