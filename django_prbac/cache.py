from django.core.cache import cache


class RoleCache:

    def __init__(self, timeout:int = 30) -> None:
        self.timeout = timeout

    def clear(self):
        cache.clear()