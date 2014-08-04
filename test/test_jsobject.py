#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from jsobject import jsobject as JS

"""Tests for jsobject."""

class JsobjectTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        self.json = """{
          "array": [
            1,
            2,
            3
          ],
          "boolean": true,
          "null": null,
          "number": 123,
          "object": {
            "a": "b",
            "c": "d",
            "e": "f"
          },
          "string": "Hello World"
        }"""
        pass

    def tearDown(self):
        pass

    def test_create_object(self):
        js = JS(self.json)
        assert type(js) == JS
