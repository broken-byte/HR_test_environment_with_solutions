from unittest import TestCase, main
import os

from greedy_algorithms.medium_problems.max_min.max_min_algs import max_min_optimized
from test_utilities.time_complexity_test_functions import process_test_file_where_lines_are_int_elements
from test_utilities.time_complexity_test_functions import get_console_time_logged_result_of

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class OptimizedMaxMinTester(TestCase):

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
        "test_4": {
            "k": 3,
            "arr": [100, 200, 300, 350, 400, 401, 402],
            "expected": 2
        },
    }

    time_complexity_test_data: dict = {
        "test_0": {
            "k": 2430,
            "test_file": "time_complexity_test_0.txt",
            "expected": 2374
        },
        "test_1": {
            "k": 90000,
            "test_file": "time_complexity_test_1.txt",
            "expected": 89733159
        }
    }

    def test_functionality_0(self):
        test_data: dict = self.get_functionality_test_data("test_0")
        k: int = test_data["k"]
        arr: list = test_data["arr"]
        expected: int = test_data["expected"]

        actual: int = max_min_optimized(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data: dict = self.get_functionality_test_data("test_1")
        k: int = test_data["k"]
        arr: list = test_data["arr"]
        expected: int = test_data["expected"]
        actual: int = max_min_optimized(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        k: int = test_data["k"]
        arr: list = test_data["arr"]
        expected: int = test_data["expected"]
        actual: int = max_min_optimized(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        k: int = test_data["k"]
        arr: list = test_data["arr"]
        expected: int = test_data["expected"]
        actual: int = max_min_optimized(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_4(self):
        test_data = self.get_functionality_test_data("test_4")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = max_min_optimized(k, arr)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_time_complexity_0(self):
        test_data: dict = self.get_time_complexity_test_data("test_0")
        arr: list = test_data["arr"]
        k = test_data["k"]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(max_min_optimized, k, arr)

        print("test_0", test_data["expected"], actual, "\n")
        self.assertEqual(expected, actual)

    def test_time_complexity_1(self):
        test_data: dict = self.get_time_complexity_test_data("test_1")
        arr: list = test_data["arr"]
        k = test_data["k"]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(max_min_optimized, k, arr)

        print("test_1", test_data["expected"], actual, "\n")
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data

    def get_time_complexity_test_data(self, test_name: str) -> dict:
        time_complexity_test_data: dict = self.time_complexity_test_data[test_name]
        test_file_path: str = test_resources_path + time_complexity_test_data["test_file"]

        arr: list = process_test_file_where_lines_are_int_elements(test_file_path, exclude_index=1)
        time_complexity_test_data["test_file"] = arr
        time_complexity_test_data["arr"] = time_complexity_test_data.pop("test_file")
        return time_complexity_test_data


if __name__ == "__main__":
    main()
