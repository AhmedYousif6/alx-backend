#!/usr/bin/env python3
""" task 5
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ cache system based on LFU algorithm
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        Call the parent class's init method.
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ store data in the cache system
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            ca = [k for k in self.usage_order if self.frequency[k] == min_freq]

            lfu_key = candidates[0]
            self.usage_order.remove(lfu_key)
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]

            print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """ get the value with given key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data.get(key)
