#!/usr/bin/python3
""" MRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Caching system MRUCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """ Assign to the self.cache_data the item value for the key.
            If key or item is None, this method should not do anything.
        """

        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                if self.mru_key:
                    print("DISCARD:", self.mru_key)
                    del self.cache_data[self.mru_key]

            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist, return None.
        """
        if key in self.cache_data:
            self.mru_key = key
            return self.cache_data[key]
        return None
