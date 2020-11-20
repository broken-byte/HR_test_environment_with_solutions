from unittest import TestCase, main, skip
import os

from searching.medium_problems.pairs.pairs_optimized import pairs_optimized
from test_utilities.time_complexity_file_processing_functions import get_console_time_logged_result_of
from test_utilities.time_complexity_file_processing_functions import process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class OptimizedPairsTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "k": 2,
            "arr": [1, 5, 3, 4, 2],
            "expected": 3
        },
        "test_1": {
            "k": 1,
            "arr": [
                363374326,
                364147530,
                61825163,
                1073065718,
                1281246024,
                1399469912,
                428047635,
                491595254,
                879792181,
                1069262793
            ],
            "expected": 0
        },
        "test_2": {
            "k": 2,
            "arr": [1, 3, 5, 8, 6, 4, 2],
            "expected": 5
        },
    }

    time_complexity_test_data: dict = {
        "test_0": {
            "k": 11324,
            "test_file": "time_complexity_test_0.txt",
            "expected": 2617
        },
        "test_1": {
            "k": 30244,
            "test_file": "time_complexity_test_1.txt",
            "expected": 3057
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = pairs_optimized(k, arr)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = pairs_optimized(k, arr)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        k: int = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = pairs_optimized(k, arr)
        self.assertEqual(expected, actual)

    def test_time_complexity_0(self):
        test_data: dict = self.get_time_complexity_test_data("test_0")
        k = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(pairs_optimized, k, arr)
        self.assertEqual(expected, actual)

    def test_time_complexity_1(self):
        test_data: dict = self.get_time_complexity_test_data("test_1")
        k = test_data["k"]
        arr: list = test_data["arr"]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(pairs_optimized, k, arr)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data

    def get_time_complexity_test_data(self, test_name: str) -> dict:
        time_complexity_test_data: dict = self.time_complexity_test_data[test_name]
        test_file_path: str = test_resources_path + time_complexity_test_data["test_file"]

        arr: list = process_test_file_where_single_line_is_an_int_array(test_file_path)
        time_complexity_test_data["test_file"] = arr
        time_complexity_test_data["arr"] = time_complexity_test_data.pop("test_file")
        return time_complexity_test_data


if __name__ == "__main__":
    main()


