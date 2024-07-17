#!/usr/bin/env python3
"""
     Writing Strings to Redis
"""
from typing import Union
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
