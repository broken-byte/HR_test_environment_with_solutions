from unittest import TestCase, main
import os

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class TreeAndNodeTester(TestCase):

    def test_tree_should_have_a_root_with_data_of_1(self):
        tree: Tree = Tree()

        expected_class: type = Node
        expected_data: int = 1

        actual_class: type = type(tree.root)
        actual_data: int = tree.root.data

        self.assertEqual(expected_class, actual_class)
        self.assertEqual(expected_data, actual_data)

    def test_that_tree_can_construct_given_indices(self):
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


if __name__ == "__main__":
    main()


