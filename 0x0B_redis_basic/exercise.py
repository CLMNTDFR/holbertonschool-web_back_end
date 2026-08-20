#!/usr/bin/env python3
"""Redis cache helpers for storing data with random keys."""
import uuid
from typing import Callable, Optional, Union

import redis


class Cache:
    """Wrap a Redis client and store values under generated keys."""

    def __init__(self) -> None:
        """Create a Redis client and wipe the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Save data in Redis under a new uuid key and return that key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """Return a Redis value, optionally converted by fn."""
        data = self._redis.get(key)
        if data is None or fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """Return a Redis value decoded as a UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Return a Redis value converted to an integer."""
        return self.get(key, fn=int)
