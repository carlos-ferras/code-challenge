from datetime import datetime, timedelta

from .utils.cache_list import DoublyLinkedListCache
from .utils.cache_node import CacheNode
from .utils.cache_types import ValueLoadCallBack, CacheKey, CacheValue
from .utils.constants import DEFAULT_MAXIMUM_CAPACITY, DEFAULT_EXPIRATION_TIME


class LRUCache:
    def __init__(
        self,
        load_callback: ValueLoadCallBack,
        maximum_capacity: int = DEFAULT_MAXIMUM_CAPACITY,
        expiration_time: int = DEFAULT_EXPIRATION_TIME
    ):
        self._load = load_callback
        self.maximum_capacity = maximum_capacity
        self.expiration_time = expiration_time
        self.cache = DoublyLinkedListCache()

    def get(self, key: CacheKey) -> CacheValue:
        if self.cache.has_node_by_key(key):
            cache_node = self.cache.get_node_by_key(key)
            if not cache_node.is_expired():
                return self._move_node_to_start(cache_node)
        return self.set(key)

    def set(self,
            key: CacheKey,
            value: CacheValue = None,
            expire_at: datetime = None,
            expiration_time: int = None) -> CacheValue:
        self.cache.delete_node_by_key(key)

        if self.cache.length == self.maximum_capacity:
            self.cache.delete_last_node()

        if value is None and self._load is not None:
            value = self._load(key)
        if expire_at is None:
            expire_at = datetime.now() + timedelta(0, expiration_time or self.expiration_time)
        self.cache.add_node(key, value, expire_at)

        return value

    def _move_node_to_start(self, cache_node: CacheNode) -> CacheValue:
        self.cache.move_node_to_start(cache_node)
        return cache_node.value
