# **Caching** :computer:

## **Description** :speech_balloon:

A caching system is a technology used to temporarily store copies of data or files in a fast-access location, with the goal of accelerating access to these data on future requests. In other words, a cache is a temporary storage layer that helps reduce the loading time of applications and websites by storing parts of data that are frequently accessed or time-consuming to generate or retrieve. This is especially useful in environments where data reading operations are much more frequent than writing operations.

## **What we should learn from this project:** :bookmark_tabs:

* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have

## **Tasks** :books:

#### **0. Basic dictionary**

Create a class BasicCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* This caching system doesn’t have limit
* def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
* def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None.

#### **1. FIFO caching**

Create a class FIFOCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        * you must discard the first item put in cache (FIFO algorithm)
        * you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None.

#### **2. LIFO Caching**

Create a class LIFOCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None.

#### **3. LRU Caching**

Create a class LRUCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None.

#### **4. MRU Caching**

Create a class MRUCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the most recently used item (MRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None.

## **Author** :black_nib:

* **Clement DEFER**



