#!/usr/bin/env python3
"""
Cache Module
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A decorator that counts how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        normalized_args = str(args)
        self._redis.rpush(inputs_key, normalized_args)

        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))

        return result
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
                                            str, bytes, int, float, None]:
        """Retrieve and optionally convert data from Redis by key."""
        value = self._redis.get(name=key)
        if value is not None and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)

    def replay(self, method: Callable):
        """ Display the history of calls of a particular function."""

        method_name = method.__qualname__
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        inputs_list = self._redis.lrange(inputs_key, 0, -1)
        outputs_list = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method_name} was called {len(inputs_list)} times:")
        for input_str, output_str in zip(inputs_list, outputs_list):
            print(f"{method_name}(*{input_str.decode('utf-8')}) ->
                  {output_str.decode('utf-8')}")
