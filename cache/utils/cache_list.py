from datetime import datetime

from .cache_node import CacheNode
from .cache_types import CacheKey, CacheValue


class DoublyLinkedListCache:
    def __init__(self):
        self.start_node = None
        self.last_node = None
        self.length = 0
        self._node_references = {}

    def add_node(self,
                 key: CacheKey,
                 value: CacheValue,
                 expire_at: datetime) -> CacheNode:
        self._node_references[key] = CacheNode(key, value, expire_at, self.start_node)
        if self.start_node is not None:
            self.start_node.previous_node = self._node_references[key]
        else:
            self.last_node = self._node_references[key]
        self.start_node = self._node_references[key]
        self.length += 1

        return self._node_references[key]

    def move_node_to_start(self, node: CacheNode) -> None:
        if node.previous_node and node == self.last_node:
            self.last_node = node.previous_node
        if node.previous_node is not None:
            node.previous_node.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous_node = node.previous_node
        node.next_node = self.start_node
        self.start_node.previous_node = node
        self.start_node = node

    def delete_node_by_key(self, key: CacheKey) -> None:
        node = self._node_references[key]
        if node.previous_node is not None:
            node.previous_node.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous_node = node.previous_node
        del self._node_references[key]
        self.length -= 1

    def delete_start_node(self) -> None:
        if self.start_node is not None:
            if self.start_node.next_node is not None:
                self.start_node.next_node.previous_node = None
            else:
                self.last_node = None
            del self._node_references[self.start_node.key]
            self.start_node = self.start_node.next_node
            self.length -= 1

    def delete_last_node(self) -> None:
        if self.last_node is not None:
            if self.last_node.previous_node is not None:
                self.last_node.previous_node.next_node = None
            else:
                self.start_node = None
            del self._node_references[self.last_node.key]
            self.last_node = self.last_node.previous_node
            self.length -= 1

    def get_node_by_key(self, key: CacheKey) -> CacheNode:
        return self._node_references[key]

    def has_node_by_key(self, key: CacheKey) -> bool:
        return key in self._node_references
