from unittest import TestCase, main
import os

from test_utilities.time_complexity_test_functions import get_console_time_logged_result_of
from test_utilities.time_complexity_test_functions import process_test_file_where_lines_are_int_arrays
from searching.medium_problems.triple_sum.tests.BruteForceTripleSumTester import BruteForceTripleSumTester
from searching.medium_problems.triple_sum.optimized_triple_sum import optimized_triple_sum

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class OptimizedTripleSumTester(TestCase):

    functionality_test_data: dict = BruteForceTripleSumTester.functionality_test_data

    time_complexity_test_data: dict = {
        "test_0": {
            "test_file": "time_complexity_test_0.txt",
            "expected": 10372982
        },
        "test_1": {
            "test_file": "time_complexity_test_1.txt",
            "expected": 9593177511025
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = optimized_triple_sum(a, b, c)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = optimized_triple_sum(a, b, c)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = optimized_triple_sum(a, b, c)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = optimized_triple_sum(a, b, c)
        self.assertEqual(expected, actual)

    def test_time_complexity_0(self):
        test_data: dict = self.get_time_complexity_test_data("test_0")
        a: list = test_data["arrays"][0]
        b: list = test_data["arrays"][1]
        c: list = test_data["arrays"][2]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(optimized_triple_sum, a, b, c)
        self.assertEqual(expected, actual)

    def test_time_complexity_1(self):
        test_data: dict = self.get_time_complexity_test_data("test_1")
        a: list = test_data["arrays"][0]
        b: list = test_data["arrays"][1]
        c: list = test_data["arrays"][2]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(optimized_triple_sum, a, b, c)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data

    def get_time_complexity_test_data(self, test_name: str) -> dict:
        time_complexity_test_data: dict = self.time_complexity_test_data[test_name]
        test_file_path: str = test_resources_path + time_complexity_test_data["test_file"]

        arrays: list = process_test_file_where_lines_are_int_arrays(test_file_path, exclude_index=0)
        time_complexity_test_data["arrays"] = arrays
        return time_complexity_test_data
