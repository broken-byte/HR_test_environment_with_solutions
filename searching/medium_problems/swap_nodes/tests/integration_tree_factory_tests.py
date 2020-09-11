from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree
from searching.medium_problems.swap_nodes.classes.TreeFactory import TreeFactory


class IntegrationTreeFactoryTester(TestCase):

    def setUp(self):
        self.tree_factory: TreeFactory = TreeFactory()

    def tearDown(self):
        self.tree_factory = None

    def test_that_tree_factory_can_construct_tree_levels_with_partitioned_indices(self):
        root: Node = Node(1)
        self.tree_factory.tree_root = root
        partitioned_indices: list = [[2, 3], [-1, -1, -1, -1]]
        self.tree_factory.partitioned_indices = partitioned_indices
        self.tree_factory.construct_tree_levels_with_partitioned_indices()

        expected: list = [
            [Node(1).data],
            [Node(2).data, Node(3).data],
            [None, None, None, None]
        ]
        actual_tree_levels: list = self.tree_factory.tree_levels
        actual_unpacked_tree_levels: list = self.unpack_tree_levels(actual_tree_levels)
        self.assertEqual(expected, actual_unpacked_tree_levels)

    def test_that_tree_factory_can_construct_tree_given_partitioned_indices(self):
        partitioned_indices: list = [[2, 3], [-1, -1, -1, -1]]
        self.tree_factory.construct_tree_with(partitioned_indices)
        constructed_tree: Tree = self.tree_factory.get_constructed_tree()
        constructed_tree.perform_in_order_traversal(constructed_tree.root)

        expected_in_order_traversal: list = [2, 1, 3]
        actual_in_order_traversal: list = constructed_tree.in_order_traversal_path
        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

    @staticmethod
    def unpack_tree_levels(tree_levels: list) -> list:
        unpacked_tree_levels: list = []
        for level in tree_levels:
            unpacked_level: list = []
            for node in level:
                unpacked_node = node.data if type(node) == Node else None
                unpacked_level.append(unpacked_node)
            unpacked_tree_levels.append(unpacked_level)
        return unpacked_tree_levels
