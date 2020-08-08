from unittest import TestCase, skip, main
import os

from .minimum_swaps_algs import min_swaps

currentPath = os.path.dirname(__file__)
testResourcesPath = currentPath + "/test_resources/"


class MinimumSwapsTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "arr": [4, 3, 1, 2],
            "expected": 3
        },
        "test_1": {
            "arr": [2, 3, 4, 1, 5],
            "expected": 3
        },
        "test_2": {
            "arr": [1, 3, 5, 2, 4, 6, 7],
            "expected": 3
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = min_swaps(arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = min_swaps(arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = min_swaps(arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()
