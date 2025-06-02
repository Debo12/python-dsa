from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.max_capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.max_capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

cache = LRUCache(2)
cache.put(1, 'A')   # Cache: {1: 'A'}
cache.put(2, 'B')   # Cache: {1: 'A', 2: 'B'}
cache.get(1)        # Access 1 → Cache: {2: 'B', 1: 'A'}
cache.put(3, 'C')   # Cache full → removes 2 → Cache: {1: 'A', 3: 'C'}
cache.get(2)        # Returns -1 (2 was removed)
