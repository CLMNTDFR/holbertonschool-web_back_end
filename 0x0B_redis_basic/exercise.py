#!/usr/bin/env python3
"""Redis cache helpers for storing data with random keys."""
import uuid
from typing import Union

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
