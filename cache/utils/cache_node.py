from datetime import datetime

from .cache_types import CacheKey, CacheValue


class CacheNode:
    def __init__(self,
                 key: CacheKey,
                 value: CacheValue,
                 expire_at: datetime,
                 next_node: 'CacheNode' = None):
        self.key = key
        self.value = value
        self.expire_at = expire_at
        self.next_node = next_node
        self.previous_node = None
    
    def is_expired(self) -> bool:
        return self.expire_at <= datetime.now()
