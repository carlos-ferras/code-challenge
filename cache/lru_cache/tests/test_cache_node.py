import unittest
from datetime import datetime, timedelta

from ..utils.cache_node import CacheNode

key = 'test_key'
value = 'test_value'
expire_at = datetime.now() + timedelta(0, 60)


class TestCacheNode(unittest.TestCase):
    def setUp(self):
        self.node = CacheNode(
            key,
            value,
            expire_at
        )

    def test_key_initialized(self):
        self.assertEqual(
            self.node.key,
            key,
            "Should initialize the node key"
        )

    def test_value_initialized(self):
        self.assertEqual(
            self.node.value,
            value,
            "Should initialize the node value"
        )

    def test_expiration_initialized(self):
        self.assertEqual(
            self.node.expire_at,
            expire_at,
            "Should initialize the node expiration date"
        )

    def test_unexpired_node(self):
        self.assertEqual(
            self.node.is_expired(),
            False,
            "Should not be expired"
        )

    def test_expired_node(self):
        self.node.expire_at = datetime.now() - timedelta(0, 60)
        self.assertEqual(
            self.node.is_expired(),
            True,
            "Should be expired"
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
