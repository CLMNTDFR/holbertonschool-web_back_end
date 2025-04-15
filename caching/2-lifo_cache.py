#!/usr/bin/python3
""" LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system LIFOCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Assign to the self.cache_data the item value for the key.
            If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                if self.last_key:
                    print("DISCARD:", self.last_key)
                    del self.cache_data[self.last_key]

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist, return None.
        """
        return self.cache_data.get(key, None)
