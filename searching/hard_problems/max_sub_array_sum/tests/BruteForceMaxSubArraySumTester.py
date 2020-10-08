import os
from unittest import TestCase, main

from searching.hard_problems.max_sub_array_sum.brute_force_max_sub_array_sum import brute_force_max_sub_array_sum

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForceMaxSubArraySumTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "a": [3, 3, 9, 9, 5],
            "m": 7,
            "expected": 6
        },
        "test_1": {
            "a": [1, 2, 3],
            "m": 2,
            "expected": 1
        },
        "test_2": {
            "a": [1, 5, 9],
            "m": 5,
            "expected": 4
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        a: list = test_data["a"]
        m: int = test_data["m"]

        expected: int = test_data["expected"]
        actual: int = brute_force_max_sub_array_sum(a, m)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        a: list = test_data["a"]
        m: int = test_data["m"]

        expected: int = test_data["expected"]
        actual: int = brute_force_max_sub_array_sum(a, m)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        a: list = test_data["a"]
        m: int = test_data["m"]

        expected: int = test_data["expected"]
        actual: int = brute_force_max_sub_array_sum(a, m)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


