from datetime import datetime, timedelta

from .utils.cache_list import DoublyLinkedListCache
from .utils.cache_node import CacheNode
from .utils.cache_types import ValueLoadCallBack, CacheKey, CacheValue
from .utils.constants import DEFAULT_MAXIMUM_CAPACITY, DEFAULT_EXPIRATION_TIME


class LRUCache:
    """LRU Cache implementation

    """

    def __init__(
        self,
        load_callback: ValueLoadCallBack,
        maximum_capacity: int = DEFAULT_MAXIMUM_CAPACITY,
        expiration_time: int = DEFAULT_EXPIRATION_TIME
    ):
        """
        :param load_callback: Method to call to load new content from the network,
            it is used if you try to get a key which does't exist yet,
            it should receive a key as argument and return the loaded value
        :param maximum_capacity: Maximum amount of nodes that the cache will store; by default it is 50000
        :param expiration_time: Maximum validity time for a node into the cache in seconds; by default it is 5184000
        """

        self._load = load_callback
        self.maximum_capacity = maximum_capacity
        self.expiration_time = expiration_time
        self.cache = DoublyLinkedListCache()

    def get(self, key: CacheKey) -> CacheValue:
        """Get the value of a cache node by its key

        :param key: Cache node identifier
        :return: Associated cache value to this key
        """

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
        """Add new or Update is exist a cache node

        :param key: Cache node identifier
        :param value: Associated cache value for this key
        :param expire_at: Expiration datetime for this node
        :param expiration_time: Maximum validity time for this node into the cache in seconds;
            if None, the default will be used.
        :return: Cache value for this node
        """
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
        """

        :param cache_node: Cache node to move
        :return: Cache node value
        """

        self.cache.move_node_to_start(cache_node)
        return cache_node.value
