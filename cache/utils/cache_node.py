from datetime import datetime

from .cache_types import CacheKey, CacheValue


class CacheNode:
    """Represent a cache element

    """

    def __init__(self,
                 key: CacheKey,
                 value: CacheValue,
                 expire_at: datetime,
                 next_node: 'CacheNode' = None):
        """
        :param key: Identifier for this node
        :param value: Cache value to store
        :param expire_at: Datetime in which this node will expire
        :param next_node: Child cache node
        """

        self.key = key
        self.value = value
        self.expire_at = expire_at
        self.next_node = next_node
        self.previous_node = None

    def is_expired(self) -> bool:
        """Check if the node value is expired

        :return: True if the node value is expired, if not, False
        """

        return self.expire_at <= datetime.now()
