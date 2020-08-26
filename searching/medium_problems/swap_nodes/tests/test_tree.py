from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree


class TreeTester(TestCase):

    node_checker_path: list = []

    def test_tree_should_have_a_root_with_data_of_1(self):
        tree: Tree = Tree()

        expected_class: type = Node
        expected_data: int = 1

        actual_class: type = type(tree.root)
        actual_data: int = tree.root.data

        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_data, actual_data)

    def test_that_tree_can_partition_indices_into_level(self):
        tree: Tree = Tree()
        indices: list = [
            [2, 3],
            [-1, -1],
            [-1, -1]
        ]
        tree.partition_indices_into_levels(indices)
        expected: list = [
            [[2, 3]],
            [[-1, -1], [-1, -1]]
        ]
        actual: list = tree.leveled_indices
        self.assertEqual(expected, actual)

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


