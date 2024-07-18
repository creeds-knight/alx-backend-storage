#!/usr/bin/env python3
"""
    Web Cache and tracker
"""
import requests
import redis
from typing import Callable
import functools


redis = redis.Redis()


def cache(method: Callable) -> Callable:
    """
        Caches the result of the get_page
    """
    @functools.wraps(method)
    def decorator(url: str) -> str:
        """
            Wrapper for caching
        """
        redis.incr(f'count:{url}')
        res = redis.get(f'res:{url')
        if res:
            return res.decode('utf-8')
        res = method(url)
        redis.set(f'count:{url}', 0)
        redis.setex(f'res:{url}', 10, res)
        return res
    return decorator


@cache
def get_page(url: str) -> str:
    """
        Returns the content of a particular url using the requests lib
    """
    try:
        response = requests.get(url)
        raise_for_status()
        return response.text
    except Exception as e:
        print(e)
