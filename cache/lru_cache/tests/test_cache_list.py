import unittest
from datetime import datetime, timedelta

from ..utils.cache_list import DoublyLinkedListCache

expire_at = datetime.now() + timedelta(0, 60)
node_data_1 = {
    'key': 'test_key1',
    'value': 'test_value1'
}
node_data_2 = {
    'key': 'test_key2',
    'value': 'test_value2'
}
node_data_3 = {
    'key': 'test_key3',
    'value': 'test_value3'
}


class TestCacheList(unittest.TestCase):
    def setUp(self):
        self.cacheList = DoublyLinkedListCache()

    def test_add_node(self):
        self.assertEqual(
            self.cacheList.has_node_by_key(node_data_1['key']),
            False,
            "Should not have the node registered"
        )
        self.assertEqual(
            self.cacheList.length,
            0,
            "Should have length=0"
        )

        self.cacheList.add_node(
            node_data_1['key'],
            node_data_1['value'],
            expire_at
        )

        self.assertEqual(
            self.cacheList.has_node_by_key(node_data_1['key']),
            True,
            "Should have the node registered"
        )

        self.assertEqual(
            self.cacheList.start_node.key,
            node_data_1['key'],
            "Should set start node as the last registered node"
        )

        self.assertEqual(
            self.cacheList.last_node.key,
            node_data_1['key'],
            "Should set last node to this node, as it is the only one registered"
        )

        self.assertEqual(
            self.cacheList.length,
            1,
            "Should have length=1"
        )

    def test_move_node_to_start(self):
        node1 = self.cacheList.add_node(
            node_data_1['key'],
            node_data_1['value'],
            expire_at
        )

        node2 = self.cacheList.add_node(
            node_data_2['key'],
            node_data_2['value'],
            expire_at
        )

        self.assertEqual(
            self.cacheList.start_node,
            node2,
            "Should set start node as the last registered node"
        )

        self.assertEqual(
            self.cacheList.last_node,
            node1,
            "Should set last node as node1"
        )

        self.assertEqual(
            node2.next_node,
            node1,
            "Should set node1 as next node in node2"
        )

        self.assertEqual(
            node1.previous_node,
            node2,
            "Should set node2 as previous node in node2"
        )

        self.cacheList.move_node_to_start(node1)

        self.assertEqual(
            self.cacheList.start_node,
            node1,
            "Should set start node as node1"
        )

        self.assertEqual(
            self.cacheList.last_node,
            node2,
            "Should set last node as node2"
        )

        self.assertEqual(
            node1.next_node,
            node2,
            "Should set node2 as next node in node1"
        )

        self.assertEqual(
            node2.previous_node,
            node1,
            "Should set node1 as previous node in node1"
        )

    def test_delete_node_by_key(self):
        node1 = self.cacheList.add_node(
            node_data_1['key'],
            node_data_1['value'],
            expire_at
        )

        self.cacheList.add_node(
            node_data_2['key'],
            node_data_2['value'],
            expire_at
        )

        node3 = self.cacheList.add_node(
            node_data_3['key'],
            node_data_3['value'],
            expire_at
        )

        self.cacheList.delete_node_by_key(node_data_2['key'])

        self.assertEqual(
            self.cacheList.has_node_by_key(node_data_2['key']),
            False,
            "Should not have the node registered"
        )

        self.assertEqual(
            node3.next_node,
            node1,
            "Should update next_node in the previous node"
        )

        self.assertEqual(
            node1.previous_node,
            node3,
            "Should update previous_node in the next node"
        )

    def test_delete_start_node(self):
        node1 = self.cacheList.add_node(
            node_data_1['key'],
            node_data_1['value'],
            expire_at
        )

        self.cacheList.add_node(
            node_data_2['key'],
            node_data_2['value'],
            expire_at
        )

        self.cacheList.delete_start_node()

        self.assertEqual(
            self.cacheList.has_node_by_key(node_data_2['key']),
            False,
            "Should not have the node registered"
        )

        self.assertEqual(
            self.cacheList.start_node,
            node1,
            "Should update start_node"
        )

    def test_delete_last_node(self):
        self.cacheList.add_node(
            node_data_1['key'],
            node_data_1['value'],
            expire_at
        )

        node2 = self.cacheList.add_node(
            node_data_2['key'],
            node_data_2['value'],
            expire_at
        )

        self.cacheList.delete_last_node()

        self.assertEqual(
            self.cacheList.has_node_by_key(node_data_1['key']),
            False,
            "Should not have the node registered"
        )

        self.assertEqual(
            self.cacheList.start_node,
            node2,
            "Should update start_node"
        )

        self.assertEqual(
            self.cacheList.last_node,
            node2,
            "Should update last_node"
        )

    def test_get_node_by_key(self):
        node1 = self.cacheList.add_node(
            node_data_1['key'],
            node_data_1['value'],
            expire_at
        )

        self.assertEqual(
            self.cacheList.get_node_by_key(node_data_1['key']),
            node1,
            "Should get a node by its key"
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
