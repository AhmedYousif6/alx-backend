#!/usr/bin/env python3
""" task 1 Module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCaching for caching system
    based on the algoeithm FIFO
    store data and get data
    """
    def __init__(self):
        """
        initialize cache dict and list to keep traking order
        """
        super().__init__()
        self.order_list = []

    def put(self, key, item):
        """
        store data in cache,
        evict first-in item if the cache reach the maximum limit
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order_list.append(key)
            self.order_list.remove(key)
            self.order_list.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in = self.order_list.pop(0)
                del self.cache_data[first_in]
                print(f"Discard: {first_in}")

    def get(self, key):
        """
        return the value linked to the given key in
        the cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
