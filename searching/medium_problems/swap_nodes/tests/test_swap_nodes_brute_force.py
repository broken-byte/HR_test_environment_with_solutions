from unittest import TestCase, main
import os

from searching.medium_problems.swap_nodes.swap_nodes_brute_force import swap_nodes_brute_force

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForceSwapNodesTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "indexes": [
                [2, 3],
                [-1, -1],
                [-1, -1]
            ],
            "queries": [1, 1],
            "expected": [
                [3, 1, 2],
                [2, 1, 3]
            ]
        },
        "test_1": {
            "indexes": [
                [2, 3],
                [4, 5],
                [6, -1],
                [-1, 7],
                [8, 9],
                [10, 11],
                [12, 13],
                [-1, 14],
                [-1, -1],
                [15, -1],
                [16, 17],
                [-1, -1],
                [-1, -1],
                [-1, -1],
                [-1, -1],
                [-1, -1],
                [-1, -1]
            ],
            "queries": [2, 3],
            "expected": [
                [14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16],
                [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15]
            ]
        },
        "test_2": {
            "indexes": [
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
            ],
            "queries": [2, 4],
            "expected": [
                [2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10],
                [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]
            ]
        },
        "test_3": {
            "indexes": [
                [2, 3],
                [-1, 4],
                [-1, 5],
                [-1, -1],
                [-1, -1]
            ],
            "queries": [2],
            "expected": [
                [4, 2, 1, 5, 3]
            ]
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        indexes: list = test_data["indexes"]
        queries: list = test_data["queries"]

        expected: list = test_data["expected"]
        actual: list = swap_nodes_brute_force(indexes, queries)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        indexes: list = test_data["indexes"]
        queries: list = test_data["queries"]

        expected: list = test_data["expected"]
        actual: list = swap_nodes_brute_force(indexes, queries)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        indexes: list = test_data["indexes"]
        queries: list = test_data["queries"]

        expected: list = test_data["expected"]
        actual: list = swap_nodes_brute_force(indexes, queries)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        indexes: list = test_data["indexes"]
        queries: list = test_data["queries"]

        expected: list = test_data["expected"]
        actual: list = swap_nodes_brute_force(indexes, queries)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


