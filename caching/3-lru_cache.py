#!/usr/bin/python3
""" LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Caching system LRUCache that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Assign to the self.cache_data the item value for the key.
            If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.key_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.key_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.key_order.remove(key)
        self.key_order.append(key)
        return self.cache_data[key]
