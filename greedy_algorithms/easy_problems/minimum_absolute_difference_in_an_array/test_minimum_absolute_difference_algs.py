from unittest import TestCase, main
import os

from greedy_algorithms.easy_problems.minimum_absolute_difference_in_an_array.minimum_absolute_difference_algs import *
from test_utilities.time_complexity_test_functions import process_test_file_where_lines_are_int_arrays
from test_utilities.time_complexity_test_functions import get_console_time_logged_result_of
from test_utilities.test_variables import console_break_line

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class MinimumDifferenceTester(TestCase):

    functionality_tests: dict = {
        "test_0": {
            "arr": [3, -7, 0],
            "expected": 3
        },
        "test_1": {
            "arr": [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75],
            "expected": 1
        },
        "test_2": {
            "arr": [1, -3, 71, 68, 17],
            "expected": 3
        },
        "test_3": {
            "arr": [-2, 2, 4],
            "expected": 2
        },
    }

    time_complexity_tests = {
        "tc_test0": {
            "testFile": "time_complexity_test_0.txt",
            "expected": 0
        }
    }

    def test_brute_force_approach(self):
        print("\nBrute Force Functionality Tests\n", console_break_line)
        for testName, testData in self.functionality_tests.items():
            arr: list = testData["arr"]
            expected: int = testData["expected"]
            actual: int = minimum_absolute_difference_brute_force(arr)
            print(testName, testData, actual, "\n")
            self.assertEqual(expected, actual)

    def test_optimized_approach(self):
        print("\nOptimized 0 Functionality Tests\n", console_break_line)
        for testName, testData in self.functionality_tests.items():
            arr: list = testData["arr"]
            expected: int = testData["expected"]
            actual: int = minimum_absolute_difference_optimized(arr)
            self.assertEqual(expected, actual)
            print(testData, actual, "\n")

    def test_time_complexity(self):
        print("\nTime Complexity Tests\n", console_break_line)
        for testName, testData in self.time_complexity_tests.items():
            test_file_path: str = test_resources_path + testData["testFile"]
            arr: list = process_test_file_where_lines_are_int_arrays(test_file_path, exclude_index=0)
            expected: int = testData["expected"]
            actual: int = get_console_time_logged_result_of(minimum_absolute_difference, arr)

            self.assertEqual(expected, actual)
            print(testName, testData, actual, "\n")


if __name__ == "__main__":
    main()
