import unittest

from ..lru_cache import LRUCache


def callback(key):
    return key


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(callback)

    def test_create_cache_node_on_get(self):
        self.cache.get('test')

        self.assertEqual(
            self.cache.cache.has_node_by_key('test'),
            True,
            "Should have the node registered"
        )

    def test_add_cache_node(self):
        self.cache.set('test', 'static value')

        self.assertEqual(
            self.cache.get('test'),
            'static value',
            "Should have the node registered"
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
