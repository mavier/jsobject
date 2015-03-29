# -*- coding: utf-8 -*-

try:
    import ujson as json
except:
    try:
        import simplejson as json
    except:
        import json

class ObjectEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Object):
                return obj.data
            return json.JSONEncoder.default(self, obj)

def dump(fp):
    return json.dump(fp, cls=ObjectEncoder, indent=4)

def dumps(s):
    return json.dumps(s, cls=ObjectEncoder, indent=4)

