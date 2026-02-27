from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache=OrderedDict()
        self.capacity=capacity

    def get(self, key_):
        if key_ not in self.cache:
            return -1
        self.cache.move_to_end(key_)
        return self.cache[key_]

    def put(self, key_, value):
        if key_ in self.cache:
            self.cache.move_to_end(key_)
        self.cache[key_]=value
        if (len(self.cache)>self.capacity):
            self.cache.popitem(last=False)
