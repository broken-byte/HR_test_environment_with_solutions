import os
from unittest import TestCase, main

from searching.hard_problems.max_sub_array_sum.optimized_max_sub_array_sum import \
    optimized_max_sub_array_sum
from searching.hard_problems.max_sub_array_sum.tests.BruteForceMaxSubArraySumTester import \
    BruteForceMaxSubArraySumTester


class OptimizedMaxSubArraySumTester(TestCase):

    functionality_test_data: dict = BruteForceMaxSubArraySumTester.functionality_test_data

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        a: list = test_data["a"]
        m: int = test_data["m"]

        expected: int = test_data["expected"]
        actual: int = optimized_max_sub_array_sum(a, m)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        a: list = test_data["a"]
        m: int = test_data["m"]

        expected: int = test_data["expected"]
        actual: int = optimized_max_sub_array_sum(a, m)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        a: list = test_data["a"]
        m: int = test_data["m"]

        expected: int = test_data["expected"]
        actual: int = optimized_max_sub_array_sum(a, m)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


