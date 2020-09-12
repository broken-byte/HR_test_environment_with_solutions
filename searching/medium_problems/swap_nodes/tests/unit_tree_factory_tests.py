from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree
from searching.medium_problems.swap_nodes.classes.TreeFactory import TreeFactory


class UnitTreeFactoryTester(TestCase):

    def setUp(self):
        self.tree_factory: TreeFactory = TreeFactory()

    def tearDown(self):
        self.tree_factory = None

    def test_that_tree_factory_can_construct_nodes_with_partition_of_non_null_data(self):
        partition: list = [2, 3]
        expected: list = [Node(2).data, Node(3).data]
        actual_nodes: list = self.tree_factory.construct_nodes_with(partition)
        actual_unpacked_nodes: list = [n.data for n in actual_nodes]
        self.assertEqual(expected, actual_unpacked_nodes)

    def test_that_tree_factory_can_construct_null_nodes_with_partition_of_null_data(self):
        partition: list = [-1, -1, -1, -1]
        expected: list = [None, None, None, None]
        actual: list = self.tree_factory.construct_nodes_with(partition)
        self.assertEqual(expected, actual)

    def test_that_tree_factory_can_connect_two_levels(self):
        self.tree_factory.tree_levels = [
            [Node(1)],
            [Node(2), Node(3)]
        ]
        self.tree_factory.connect(self.tree_factory.tree_levels[0], self.tree_factory.tree_levels[1])
        actual: bool = self.is_tree_connected(self.tree_factory.tree_levels[0],
                                              self.tree_factory.tree_levels[1])
        self.assertTrue(actual)

    @staticmethod
    def is_tree_connected(tree_level_0, tree_level_1) -> bool:
        for node in tree_level_0:
            left_index: int = 0
            right_index: int = 1
            for _ in range(len(tree_level_1)//2):
                if node.left != tree_level_1[left_index]:
                    return False
                if node.right != tree_level_1[right_index]:
                    return False
        return True
