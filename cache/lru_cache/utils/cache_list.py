from datetime import datetime

from .cache_node import CacheNode
from .cache_types import CacheKey, CacheValue


class DoublyLinkedListCache:
    """Logic structure to store the cache elements

    """

    def __init__(self):
        self.start_node = None
        self.last_node = None
        self.length = 0
        self._node_references = {}

    def add_node(self,
                 key: CacheKey,
                 value: CacheValue,
                 expire_at: datetime) -> CacheNode:
        """Add a new cache node at the beginning of the cache

        :param key: Identifier for the new node
        :param value: Cache value to store
        :param expire_at: Datetime in which this node will expire
        :return: The created cache node
        """

        self._node_references[key] = CacheNode(key, value, expire_at, self.start_node)
        if self.start_node is not None:
            self.start_node.previous_node = self._node_references[key]
        else:
            self.last_node = self._node_references[key]
        self.start_node = self._node_references[key]
        self.length += 1

        return self._node_references[key]

    def move_node_to_start(self, node: CacheNode) -> None:
        """Move a node to the beginning of the cache

        :param node: Cache node to move
        """

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
        """Delete a cache node by its key

        :param key: Cache node identifier
        """

        if self.start_node is not None and key == self.start_node.key:
            return self.delete_start_node()
        elif self.last_node is not None and key == self.last_node.key:
            return self.delete_last_node()
        elif self.has_node_by_key(key):
            node = self._node_references[key]
            if node.previous_node is not None:
                node.previous_node.next_node = node.next_node
            if node.next_node is not None:
                node.next_node.previous_node = node.previous_node
            del self._node_references[key]
            self.length -= 1

    def delete_start_node(self) -> None:
        """Delete the first node in the cache
        """

        if self.start_node is not None:
            if self.start_node.next_node is not None:
                self.start_node.next_node.previous_node = None
            else:
                self.last_node = None
            del self._node_references[self.start_node.key]
            self.start_node = self.start_node.next_node
            self.length -= 1

    def delete_last_node(self) -> None:
        """Delete the las node in the cache
        """

        if self.last_node is not None:
            if self.last_node.previous_node is not None:
                self.last_node.previous_node.next_node = None
            else:
                self.start_node = None
            del self._node_references[self.last_node.key]
            self.last_node = self.last_node.previous_node
            self.length -= 1

    def get_node_by_key(self, key: CacheKey) -> CacheNode:
        """Return a node by its key

        :param key: Cache node identifier
        :return: A cache node
        """

        # TODO: Use the linked cache nodes list for the search
        return self._node_references[key]

    def has_node_by_key(self, key: CacheKey) -> bool:
        """Check if there is a node under an specific key

        :param key: Cache node identifier
        :return: True if there is a node under this key, if not, False
        """

        return key in self._node_references
