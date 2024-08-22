#!/usr/bin/env python3
""" task 2 module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ cache system based on LIFO algorithm
    store data and
    get data from the cache system
    """
    def __init__(self):
        """
        initialize base class and order list
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        store data into cache system,
        using lifo to make room if the cache is full
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last_in = self.order.pop()
                    del self.cache_data[last_in]
                    print(f"Discard: {last_in}")
                self.order.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
        method to retrive the value,
        with a given key
        """
        return self.cache_data.get(key, None)
