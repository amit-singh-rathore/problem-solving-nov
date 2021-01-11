from collections import OrderedDict
 
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        if capacity <= 0:
            raise ValueError("capacity > 0")
        self.capacity = capacity
 
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
            
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

