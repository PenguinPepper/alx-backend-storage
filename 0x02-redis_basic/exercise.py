#!/usr/bin/env python3
"""Module contains a class named Cache"""

import redis
import uuid
from typing import Any


class Cache:
    """Class named Cache wthat sets r to redis server"""
    def __init__(self):
        self._redis = redis.Redis()

    def store(self, data: Any) -> str:
        """Method that takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
