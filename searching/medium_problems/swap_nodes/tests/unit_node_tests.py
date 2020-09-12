from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node


class UnitNodeTester(TestCase):

    def test_that_node_has_data(self):
        node: Node = Node(1)

        expected: int = 1
        actual: int = node.data

        self.assertEqual(expected, actual)

    def test_that_node_has_left_node(self):
        root_node: Node = Node(1)
        left_node: Node = Node(2)
        root_node.left = left_node

        expected: Node = left_node
        actual: Node = root_node.left

        self.assertEqual(expected, actual)

    def test_that_node_has_right_node(self):
        root_node: Node = Node(1)
        right_node: Node = Node(3)
        root_node.right = right_node

        expected: Node = right_node
        actual: Node = root_node.right

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()


