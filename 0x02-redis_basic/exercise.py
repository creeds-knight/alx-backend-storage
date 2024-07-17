#!/usr/bin/env python3
"""
     Writing Strings to Redis
"""
from typing import Union, Callable, Optional
import redis
import uuid


class Cache:
    """
        Cache definition
    """

    def __init__(self):
        """
            Initializing an instance of redis databases and flushing it
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Store the data to the database
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
            Converting data back to desired format after retrieval
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
            Retrieves a string value from a redis data storage
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
            Retrieves an integer value from a redis data storage
        """
        return self.get(key, lambda x: int(x))
