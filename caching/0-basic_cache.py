#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching system BasicCache that inherits from BaseCaching.
    """
    def put(self, key, item):
        """ Assign to the self.cache_data the item value for the key.
            If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist, return None.
        """
        return self.cache_data.get(key, None)
