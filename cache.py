import time


class Cache(object):

    def __init__(self, timeout=None):
        self._store = {}
        self._timeout = timeout

    def set(self, key, value, timeout=None):
        if not timeout:
            timeout = self._timeout
        if timeout:
            timeout = time.time() + timeout
        self._store[key] = (value, timeout)

    def get(self, key, default=None):
        data = self._store.get(key)
        if not data:
            return default
        value, expire = data
        if expire and time.time() > expire:
            del self._store[key]
            return default
        return value
