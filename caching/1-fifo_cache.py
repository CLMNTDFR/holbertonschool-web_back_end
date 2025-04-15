#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system FIFOCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Assign to the self.cache_data the item value for the key.
            If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys_order:
                self.keys_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.keys_order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist, return None.
        """
        return self.cache_data.get(key, None)
