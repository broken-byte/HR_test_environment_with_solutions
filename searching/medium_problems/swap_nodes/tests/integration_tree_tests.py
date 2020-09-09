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

    def test_that_tree_can_perform_swap_operations_with_processed_queries(self):
        indices: list = [
            [2, 3],
            [4, -1],
            [5, -1],
            [6, -1],
            [7, 8],
            [-1, 9],
            [-1, -1],
            [10, 11],
            [-1, -1],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        unprocessed_queries: list = [2, 4]
        self.tree.process_swap_queries(unprocessed_queries)
        self.tree.perform_swap_operations_with_all_processed_queries()
        expected_in_order_traversal_results: list = [
            [2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10],
            [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]
        ]
        actual_in_order_traversal_results: list = self.tree.results
        self.assertEqual(expected_in_order_traversal_results, actual_in_order_traversal_results)

    def test_that_tree_can_perform_swaps_with_swap_operations(self):
        indices: list = [
            [2, 3],
            [-1, 4],
            [-1, 5],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        processed_query: list = [2]
        self.tree.perform_swap_operations_with(processed_query)
        self.tree.perform_in_order_traversal(self.tree.root)

        expected_in_order_traversal: list = [4, 2, 1, 5, 3]
        actual_in_order_traversal: list = self.tree.in_order_traversal_path
        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

    def test_that_tree_can_swap_a_level(self):
        indices: list = [
            [2, 3],
            [-1, -1],
            [-1, -1]
        ]
        self.tree.construct_with(indices)
        tree_level_index: int = 0
        self.tree.swap_nodes_in_tree_level_with(tree_level_index)
        expected_in_order_traversal: list = [3, 1, 2]
        self.tree.perform_in_order_traversal(self.tree.root)
        actual_in_order_traversal: list = self.tree.in_order_traversal_path
        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

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
        self.tree.perform_in_order_traversal(self.tree.root)

        expected_in_order_traversal: list = [2, 1, 3]
        actual_in_order_traversal: list = self.tree.in_order_traversal_path
        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

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
