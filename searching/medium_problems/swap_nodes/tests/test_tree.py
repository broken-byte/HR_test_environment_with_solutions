from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree


class TreeTester(TestCase):

    node_checker_path: list = []
    tree_levels: list = []

    def test_tree_should_have_a_root_with_data_of_1(self):
        tree: Tree = Tree()

        expected_class: type = Node
        expected_data: int = 1

        actual_class: type = type(tree.root)
        actual_data: int = tree.root.data

        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_data, actual_data)

    def test_that_tree_can_partition_indices_into_levels(self):
        tree: Tree = Tree()
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        tree.indices = indices
        tree.partition_indices_into_levels()

        expected: list = [
            [[2, 3]],
            [[-1, -1], [-1, -1]]
        ]
        actual: list = tree.partitioned_indices
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_a_size_1_partition_with_a_level_number(self):
        tree: Tree = Tree()
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        tree.indices = indices

        expected: list = [[2, 3]]
        actual: list = tree.construct_partition_with(level_number=0)
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_a_size_2_partition_with_a_level_number(self):
        tree: Tree = Tree()
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        tree.indices = indices

        expected: list = [[-1, -1], [-1, -1]]
        actual: list = tree.construct_partition_with(level_number=1)
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_nodes_with_partition_of_non_null_data(self):
        tree: Tree = Tree()
        partition: list = [[2, 3]]
        expected: list = [(Node(2).data, Node(3).data)]
        actual_nodes: list = tree.construct_nodes_with(partition)
        actual_unpacked_nodes: list = [(pair[0].data, pair[1].data) for pair in actual_nodes]
        self.assertEqual(expected, actual_unpacked_nodes)

    def test_that_tree_can_construct_null_nodes_with_partition_of_null_data(self):
        tree: Tree = Tree()
        partition: list = [[-1, -1], [-1, -1]]
        expected: list = [(None, None), (None, None)]
        actual: list = tree.construct_nodes_with(partition)
        self.assertEqual(expected, actual)

    def test_that_tree_can_construct_tree_levels_with_partitioned_indices(self):
        tree: Tree = Tree()
        indices: list = [[2, 3], [-1, -1], [-1, -1]]
        tree.indices = indices
        tree.partition_indices_into_levels()
        tree.construct_tree_levels_with_partitioned_indices()

        expected: list = [
            [Node(1).data],
            [(Node(2).data, Node(3).data)],
            [(None, None), (None, None)]
        ]
        self.tree_levels.clear()
        actual_tree_levels: list = tree.tree_levels
        self.tree_levels = actual_tree_levels
        # TODO: Rewrite node level construction be sequentially ordered, instead of in pairs
        # self.assertEqual(expected, actual_unpacked_tree_levels)


    def test_that_tree_can_construct_given_indices(self):
        self.node_checker_path.clear()
        tree: Tree = Tree()
        indices: list = [
            [2, 3],
            [-1, -1],
            [-1, -1]
        ]
        tree.construct_with(indices)
        expected: list = [1, 2, 3]
        self.node_checker(tree.root)
        actual: list = self.node_checker_path
        self.assertEqual(expected, actual)

    def test_that_tree_can_traverse_in_order_given_indices(self):
        tree: Tree = Tree()
        indices: list = [
                [2, 3],
                [-1, -1],
                [-1, -1]
            ]
        tree.construct_with(indices)

        expected: list = [2, 1, 3]
        actual: list = tree.get_in_order_traversal()

        self.assertEqual(expected, actual)

    def node_checker(self, current_node: Node):
        self.node_checker_path.append(current_node.data)

        if current_node.left is not None:
            self.node_checker(current_node.left)
        if current_node.right is not None:
            self.node_checker(current_node.right)


if __name__ == "__main__":
    main()


