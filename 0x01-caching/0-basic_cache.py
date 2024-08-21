#!/usr/bin/env python3
""" task 0
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ caching system to put and get data
    """
    def put(self, key, item):
        """ store data to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ retrive item from cache by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
