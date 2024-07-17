#!/usr/bin/env python3
"""
     Writing Strings to Redis
"""
from typing import Union, Callable, Optional, Any
import redis
import uuid
import functools


def count_calls(method: Callable) -> Callable:
    """
        Function to count keys stored in the database
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
        Tracks the call details of a method in cache class
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
            Returns the methods output after storing ite inputs and outputs
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, result)

        return result
    return wrapper


def replay(fn: Callable) -> None:
    '''
    this displays the call history of a Cache class' method.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    in_key = '{}:inputs'.format(fxn_name)
    out_key = '{}:outputs'.format(fxn_name)
    fxn_call_count = 0
    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))
    print('{} was called {} times:'.format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fxn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))


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

    @call_history
    @count_calls
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
