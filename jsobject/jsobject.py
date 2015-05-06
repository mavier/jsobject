# -*- coding: utf-8 -*-

class Object(dict):
    def __getattr__(self, k):
        try:
            return self[k]
        except:
            return self.__getitem__(k)

    def __setattr__(self, k, v):
        if type(v) == dict:
            self[k] = self.__class__(v)
        else:
            self[k] = v
"""
add merge

from copy import deepcopy

d1 = {'a': {'b':{'c':'d'}}, 'e': {'b':{'c':'d', 'e':3}}} 
d2 = {'b': {'b':{'c':{'d':'1'}}}, 'e':{'b':{'c':{'d':"2"}}}}



def merge(a, b, path=None):
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a

def dict_merge(a, b):
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.iteritems():
        if k in result and isinstance(result[k], dict):
                result[k] = dict_merge(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result

print dict_merge(d1, d2)
print dict_merge(d2, d1)

"""
