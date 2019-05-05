import unittest

from ..lru_cache_distributed import LRUCacheDistributed


def callback(key):
    return key


class TestLRUCacheDistributed(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCacheDistributed(
            callback,
            55555,
            55555,
            55555,
            ('192.168.1.1', 5555),
            ('', 5555),
        )

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
