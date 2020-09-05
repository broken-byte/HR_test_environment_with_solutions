from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree


class IntegrationTreeTester(TestCase):

    def setUp(self):
        self.tree = Tree()
        self.node_checker_path: list = []

    def tearDown(self):
        self.tree = None
        self.node_checker_path.clear()

    def test_that_tree_can_perform_swaps_with_swap_operations(self):
        indices: list = [
            [2, 3],
            [-1, 4],
            [-1, 5],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        expected: list = [
            [Node(1).data],
            [Node(2).data, Node(3).data],
            [Node(4).data, None, Node(5).data, None],
            [None, None, None, None]
        ]
        level_indices_to_be_swapped: list = [2]
        self.tree.perform_swaps_with(level_indices_to_be_swapped)
        actual_tree_levels: list = self.tree.tree_levels
        actual_unpacked_tree_levels: list = self.unpack_tree_levels(actual_tree_levels)
        self.assertEqual(expected, actual_unpacked_tree_levels)

    def test_that_tree_can_swap_a_level(self):
        indices: list = [
            [2, 3],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        self.tree.swap_nodes_in_tree_level_with(0)
        expected_tree_level_data: list = [3, 2]
        expected_tree_level_data: list = [3, 2]
        actual_tree_level_data: list = [node.data for node in self.tree.tree_levels[1]]
        self.assertEqual(expected_tree_level_data, actual_tree_level_data)

    def test_that_tree_can_construct_tree_levels_with_partitioned_indices(self):
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        self.tree.indices = indices
        self.tree.partition_indices_into_levels()
        self.tree.construct_tree_levels_with_partitioned_indices()

        expected: list = [
            [Node(1).data],
            [Node(2).data, Node(3).data],
            [None, None, None, None]
        ]
        actual_tree_levels: list = self.tree.tree_levels
        actual_unpacked_tree_levels: list = self.unpack_tree_levels(actual_tree_levels)
        self.assertEqual(expected, actual_unpacked_tree_levels)

    def test_that_tree_can_construct_given_indices(self):
        indices: list = [
            [2, 3],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        expected: list = [1, 2, 3]
        self.connection_checker(self.tree.root)
        actual: list = self.node_checker_path
        self.assertEqual(expected, actual)

    def test_that_tree_can_traverse_in_order_given_indices(self):
        indices: list = [
            [2, 3],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        self.tree.perform_in_order_traversal(self.tree.root)

        expected: list = [2, 1, 3]
        actual: list = self.tree.in_order_traversal_path

        self.assertEqual(expected, actual)

    def connection_checker(self, current_node: Node):
        self.node_checker_path.append(current_node.data)

        if current_node.left is not None:
            self.connection_checker(current_node.left)
        if current_node.right is not None:
            self.connection_checker(current_node.right)

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
