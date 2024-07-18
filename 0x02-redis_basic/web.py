#!/usr/bin/env python3
"""
    Web Cache and tracker
"""
import requests
import redis
from typing import Callable

redis = redis.Redis()


def count_url(method: Callable) -> Callable:
    """
        Counts the number of times a url was accessed
    """
    def wrapper(url: str) -> str:
        """
            Counts
        """
        count_key = f"count:{url}"
        redis.incr(count_key)
        return method(url)
    return wrapper


def cache(expire: int = 10) -> Callable:
    """
        Caches the result of the get_page
    """
    def decorator(method: Callable) -> Callable:
        def wrapper(url: str) -> str:
            cache_key = f"cache:{url}"
            cache_content = redis.get(cache_key)
            if cache_content:
                return cache_content.decode('utf-8')
            res = method(url)
            if res is not None:
                redis.setex(cache_key, expire, res)
            return res
        return wrapper
    return decorator


@count_url
@cache(expire=10)
def get_page(url: str) -> str:
    """
        Returns the content of a particular url using the requests lib
    """
    try:
        response = requests.get(url)
        if response.status == 200:
            return response.text
        else:
            raise_for_status()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/ \
           https://www.example.com"
    print(get_page(url))
    print(get_page(url))
    print(redis.get(f"count:{url}"))
