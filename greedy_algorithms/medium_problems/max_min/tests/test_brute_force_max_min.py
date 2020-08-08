from unittest import TestCase, skip, main
import os

from ..max_min_algs import max_min_brute_force_approach

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForceMaxMinTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "k": 2,
            "arr": [1, 4, 7, 2],
            "expected": 1
        },
        "test_1": {
            "k": 3,
            "arr": [10, 100, 300, 200, 1000, 20, 30],
            "expected": 20
        },
        "test_2": {
            "k": 4,
            "arr": [1, 2, 3, 4, 10, 20, 30, 40, 100, 200],
            "expected": 3
        },
        "test_3": {
            "k": 2,
            "arr": [1, 2, 1, 2, 1],
            "expected": 0
        },
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_min_brute_force_approach(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_min_brute_force_approach(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_min_brute_force_approach(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_min_brute_force_approach(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()
