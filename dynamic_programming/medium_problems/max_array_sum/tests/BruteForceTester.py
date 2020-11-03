from unittest import TestCase, main

from dynamic_programming.medium_problems.max_array_sum.brute_force import max_subset_sum


class BruteForceTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "arr": [-2, 1, 3, -4, 5],
            "expected": 8
        },
        "test_1": {
            "arr": [3, 7, 4, 6, 5],
            "expected": 13
        },
        "test_2": {
            "arr": [2, 1, 5, 8, 4],
            "expected": 11
        },
        "test_3": {
            "arr": [3, 5, -7, 8, 10],
            "expected": 15
        },
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_subset_sum(arr)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_subset_sum(arr)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_subset_sum(arr)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_subset_sum(arr)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


