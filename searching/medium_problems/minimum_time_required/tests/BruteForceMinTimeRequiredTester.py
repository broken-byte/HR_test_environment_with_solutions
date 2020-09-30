from unittest import TestCase, main
import os

from searching.medium_problems.minimum_time_required.minimum_time_required_brute_force import min_time_brute_force

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForceMinTimeRequiredTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "machines": [2, 3],
            "goal": 5,
            "expected": 6
        },
        "test_1": {
            "machines": [1, 3, 4],
            "goal": 10,
            "expected": 7
        },
        "test_2": {
            "machines": [4, 5, 6],
            "goal": 12,
            "expected": 20
        },
        "test_3": {
            "machines": [2, 3, 2],
            "goal": 10,
            "expected": 8
        },
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = min_time_brute_force(machines, goal)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = min_time_brute_force(machines, goal)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = min_time_brute_force(machines, goal)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        machines: list = test_data["machines"]
        goal: int = test_data["goal"]

        expected: int = test_data["expected"]
        actual: int = min_time_brute_force(machines, goal)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


