from unittest import TestCase, main

from searching.medium_problems.swap_nodes.classes.Node import Node
from searching.medium_problems.swap_nodes.classes.Tree import Tree


class UnitTreeTester(TestCase):

    def setUp(self):
        self.tree = Tree()

    def tearDown(self):
        self.tree = None

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


if __name__ == "__main__":
    main()


