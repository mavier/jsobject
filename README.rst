.. image:: https://pypip.in/version/jsobject/badge.svg
    :target: https://pypi.python.org/pypi/jsobject/
    :alt: Latest Version

.. image:: https://pypip.in/download/jsobject/badge.svg
    :target: https://pypi.python.org/pypi/jsobject/
    :alt: Downloads

.. image:: https://pypip.in/py_versions/jsobject/badge.svg
    :target: https://pypi.python.org/pypi/jsobject/
    :alt: Supported Python versions

.. image:: https://pypip.in/license/jsobject/badge.svg
    :target: https://pypi.python.org/pypi/jsobject/
    :alt: License

.. image:: https://pypip.in/status/jsobject/badge.svg
    :target: https://pypi.python.org/pypi/jsobject/
    :alt: Development Status

jsobject: Objects for Humans
============================

jsobject is simple implementation JavaScript-Style Objects in Python. It is distributed as a single file module and has no dependencies other than the `Python Standard Library <http://docs.python.org/library/>`_.

Homepage and documentation: https://mavier.github.io/jsobject


Example: "Hello World" with jsobject
------------------------------------

.. code-block:: python

  from jsobject import Object
  data = {
    "boolean": True,
    "null": None,
    "number": 123,
    "objectA": {'a': 'b', 'c': {'d': 'e', 'f': {'g': 'h'}}}
    }

  jso = Object(data)

  print(jso.boolean)       # True
  print(jso.null)          # None
  print(jso.number)        # 123
  print(jso.objectA)       # {'a': 'b', 'c': {'d': 'e', 'f': {'g': 'h'}}}
  print(jso.objectA.a)     # b
  print(jso.objectA.c.d)   # e
  print(jso.objectA.c.f.g) # h

Download and Install
--------------------

Install the latest stable release with ``pip install jsobject``, ``easy_install -U jsobject`` or download `jsobject.py <https://github.com/mavier/jsobject/raw/master/jsobject.py>`__ (unstable) into your project directory. There are no hard dependencies other than the Python standard library. Jsobject runs with **Python 2.6+ and 3.x**.

Testing
_______

To run the tests use the `nosetest`.

.. image:: https://travis-ci.org/mavier/jsobject.png?branch=master
    :target: https://travis-ci.org/mavier/jsobject

.. image:: https://coveralls.io/repos/mavier/jsobject/badge.png
    :target: https://coveralls.io/r/mavier/jsobject


License
-------

Code and documentation are available according to the `MIT License <https://raw.github.com/mavier/jsobject/master/LICENSE>`__.

https://docs.python.org/3/library/json.html
https://docs.python.org/2/library/functions.html
https://docs.python.org/2/library/collections.html
https://docs.python.org/2/library/json.html

