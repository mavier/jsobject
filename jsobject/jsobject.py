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
