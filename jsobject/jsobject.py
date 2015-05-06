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

    def merge(self, mapping):
        for key in mapping:
            if key not in self:
                self[key] = mapping[key]
                continue;

            if isinstance(self[key], dict) and isinstance(mapping[key], dict):
                self[key].merge(mapping[key])
            elif isinstance(self[key], list) and isinstance(mapping[key], list):
                self[key].extend(mapping[key])
            elif self[key] == mapping[key]:
                pass
            else:
                self[key] = mapping[key]
                # raise Exception('Conflict')
