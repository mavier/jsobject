# -*- coding: utf-8 -*-

try:
    import ujson as json
except:
    try:
        import simplejson as json
    except:
        import json

from jsobject import Object


def load(fp):
    return json.load(fp, object_hook=Object)

def loads(s):
    return json.loads(s, object_hook=Object)
