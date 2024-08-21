#!/usr/bin/env python3
""" task 3
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ cache system based on LRU algorithm
    """
    def __init__(self):
        """ initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ store data
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)
        else:
            self.order.remove(key)
            self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = self.order.pop(0)
            del self.cache_data[lru]
            print(f"Discard: {lru}")

    def get(self, key):
        """ get the value with given key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
