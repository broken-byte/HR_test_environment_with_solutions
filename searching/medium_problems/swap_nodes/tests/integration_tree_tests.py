from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree
from searching.medium_problems.swap_nodes.classes.TreeFactory import TreeFactory
from searching.medium_problems.swap_nodes.classes.IndicesPartitioner import IndicesPartitioner
from searching.medium_problems.swap_nodes.classes.QueryProcessor import QueryProcessor


class IntegrationTreeTester(TestCase):

    def setUp(self):
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
        self.indices_partitioner: IndicesPartitioner = IndicesPartitioner(indices)
        partitioned_indices: list = self.indices_partitioner.partition_indices()

        self.tree_factory = TreeFactory()
        self.tree_factory.construct_tree_with(partitioned_indices)
        self.tree = self.tree_factory.get_constructed_tree()

        self.node_checker_path: list = []

    def tearDown(self):
        self.indices_partitioner = None
        self.tree_factory = None
        self.tree = None
        self.node_checker_path.clear()

    def test_that_tree_can_perform_swapped_traversals_with_processed_queries(self):
        queries: list = [2, 4]
        query_processor: QueryProcessor = QueryProcessor(queries)
        processed_queries: list = query_processor.process_queries_with_depth_limit(5)
        self.tree.perform_swapped_traversals_with(processed_queries)

        expected_in_order_traversal_results: list = [
            [2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10],
            [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]
        ]
        actual_in_order_traversal_results: list = self.tree.results

        self.assertEqual(expected_in_order_traversal_results, actual_in_order_traversal_results)

    def test_that_tree_can_perform_swaps_with_swap_operations(self):
        processed_query: list = [2]
        self.tree.perform_swap_operations_with(processed_query)
        self.tree.perform_in_order_traversal(self.tree.root)

        expected_in_order_traversal: list = [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]
        actual_in_order_traversal: list = self.tree.in_order_traversal_path

        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

    def test_that_tree_can_swap_a_level(self):
        tree_level_index: int = 1
        self.tree.swap_nodes_in_tree_level_with(tree_level_index)

        expected_in_order_traversal: list = [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]
        self.tree.perform_in_order_traversal(self.tree.root)
        actual_in_order_traversal: list = self.tree.in_order_traversal_path

        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

    def test_that_tree_can_traverse_in_order(self):
        self.tree.perform_in_order_traversal(self.tree.root)

        expected: list = [6, 9, 4, 2, 1, 7, 5, 10, 8, 11, 3]
        actual: list = self.tree.in_order_traversal_path

        self.assertEqual(expected, actual)

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
