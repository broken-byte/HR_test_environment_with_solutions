from unittest import TestCase, main
import os

from test_utilities.time_complexity_test_functions import get_console_time_logged_result_of
from test_utilities.time_complexity_test_functions import process_test_file_where_lines_are_int_arrays
from searching.medium_problems.minimum_time_required.tests.BruteForceMinTimeRequiredTester import \
    BruteForceMinTimeRequiredTester
from searching.medium_problems.minimum_time_required.optimized_min_time_required import optimized_min_time

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class OptimizedMinTimeTester(TestCase):

    functionality_test_data: dict = BruteForceMinTimeRequiredTester.functionality_test_data

    time_complexity_test_data: dict = {
        "test_0": {
            "test_file": "time_complexity_test_0.txt",
            "goal": 927,
            "expected": 45261
        },
        "test_1": {
            "test_file": "time_complexity_test_1.txt",
            "goal": 232897690,
            "expected": 1340828872701
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = optimized_min_time(machines, goal)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_0")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = optimized_min_time(machines, goal)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_0")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = optimized_min_time(machines, goal)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_0")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = optimized_min_time(machines, goal)
        self.assertEqual(expected, actual)

    def test_time_complexity_0(self):
        test_data: dict = self.get_time_complexity_test_data("test_0")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(optimized_min_time, machines, goal)
        self.assertEqual(expected, actual)

    def test_time_complexity_1(self):
        test_data: dict = self.get_time_complexity_test_data("test_1")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = get_console_time_logged_result_of(optimized_min_time, machines, goal)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data

    def get_time_complexity_test_data(self, test_name: str) -> dict:
        time_complexity_test_data: dict = self.time_complexity_test_data[test_name]
        test_file_path: str = test_resources_path + time_complexity_test_data["test_file"]

        machines: list = process_test_file_where_lines_are_int_arrays(test_file_path)
        time_complexity_test_data["machines"] = machines
        return time_complexity_test_data
