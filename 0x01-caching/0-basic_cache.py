#!/usr/bin/env python3
""" BasicCache Module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """
    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            Key
            Item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
