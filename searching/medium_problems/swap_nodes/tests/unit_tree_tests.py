from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree


class UnitTreeTester(TestCase):

    def setUp(self):
        self.tree = Tree()

    def tearDown(self):
        self.tree = None

    def test_tree_should_have_a_root_with_data_of_1(self):
        expected_class: type = Node
        expected_data: int = 1

        actual_class: type = type(self.tree.root)
        actual_data: int = self.tree.root.data

        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_data, actual_data)

    def test_that_tree_can_partition_indices_into_levels(self):
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        self.tree.indices = indices
        self.tree.partition_indices_into_levels()

        expected: list = [
            [2, 3],
            [-1, -1, -1, -1]
        ]
        actual: list = self.tree.partitioned_indices
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_a_size_1_partition_with_index_and_number_of_non_null_nodes(self):
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        self.tree.indices = indices

        expected: list = [2, 3]
        actual: list = self.tree.construct_partition_with(current_index=0, count_of_non_null_nodes_in_previous_level=1)
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_a_size_2_partition_with_index_and_number_of_non_null_nodes(self):
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        self.tree.indices = indices

        expected: list = [-1, -1, -1, -1]
        actual: list = self.tree.construct_partition_with(current_index=1, count_of_non_null_nodes_in_previous_level=2)
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_nodes_with_partition_of_non_null_data(self):
        partition: list = [2, 3]
        expected: list = [Node(2).data, Node(3).data]
        actual_nodes: list = self.tree.construct_nodes_with(partition)
        actual_unpacked_nodes: list = [n.data for n in actual_nodes]
        self.assertEqual(expected, actual_unpacked_nodes)

    def test_that_tree_can_construct_null_nodes_with_partition_of_null_data(self):
        partition: list = [-1, -1, -1, -1]
        expected: list = [None, None, None, None]
        actual: list = self.tree.construct_nodes_with(partition)
        self.assertEqual(expected, actual)

    def test_that_tree_can_connect_two_levels(self):
        self.tree.tree_levels = [
            [Node(1)],
            [Node(2), Node(3)]
        ]
        self.tree.connect(self.tree.tree_levels[0], self.tree.tree_levels[1])
        actual: bool = self.check_connections_between_levels(self.tree.tree_levels[0], self.tree.tree_levels[1])
        self.assertTrue(actual)

    def test_that_tree_can_store_proper_depth(self):
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        self.tree.construct_with(indices)
        expected: int = 2
        actual: int = self.tree.depth
        self.assertEqual(expected, actual)

    def test_that_tree_can_process_queries_1_1(self):
        swap_queries: list = [1, 1]
        self.tree.depth = 2
        self.tree.process_swap_queries(swap_queries)
        expected: list = [
            [1, 2],
            [1, 2]
        ]
        actual: list = self.tree.processed_queries
        self.assertEqual(expected, actual)

    def test_that_tree_can_process_queries_2_4(self):
        swap_queries: list = [2, 4]
        self.tree.depth = 5
        self.tree.process_swap_queries(swap_queries)
        expected: list = [
            [2, 4],
            [4]
        ]
        actual: list = self.tree.processed_queries
        self.assertEqual(expected, actual)

    @staticmethod
    def check_connections_between_levels(tree_level_0, tree_level_1) -> bool:
        for node in tree_level_0:
            left_index: int = 0
            right_index: int = 1
            for _ in range(len(tree_level_1)//2):
                if node.left != tree_level_1[left_index]:
                    return False
                if node.right != tree_level_1[right_index]:
                    return False
        return True


if __name__ == "__main__":
    main()


