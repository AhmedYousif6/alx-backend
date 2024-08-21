#!/usr/bin/env python3
""" task 4
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ cache system based on MRU algorithm
    """
    def __init__(self):
        """ initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ store data to cache system
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru = self.order.pop(-2)
            del self.cache_data[mru]
            print(f"Discard: {mru}")

    def get(self, key):
        """ get the value by given key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
