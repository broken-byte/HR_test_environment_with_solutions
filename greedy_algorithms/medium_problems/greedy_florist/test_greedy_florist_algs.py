from unittest import TestCase, skip, main

from greedy_algorithms.medium_problems.greedy_florist.greedy_florist_algs import get_minimum_cost_brute_force_approach


class GreedyFloristTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "Number of Friends": 3,
            "Flower Cost Array": [2, 5, 6],
            "expected": 13
        },
        "test_1": {
            "Number of Friends": 2,
            "Flower Cost Array": [2, 5, 6],
            "expected": 15
        },
        "test_2": {
            "Number of Friends": 3,
            "Flower Cost Array": [1, 3, 5, 7, 9],
            "expected": 29
        },
        "test_3": {
            "Number of Friends": 3,
            "Flower Cost Array": [1, 2, 3, 4],
            "expected": 11
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        k: int = test_data["Number of Friends"]
        c: list = test_data["Flower Cost Array"]

        expected: int = test_data["expected"]
        actual: int = get_minimum_cost_brute_force_approach(k, c)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        k: int = test_data["Number of Friends"]
        c: list = test_data["Flower Cost Array"]

        expected: int = test_data["expected"]
        actual: int = get_minimum_cost_brute_force_approach(k, c)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        k: int = test_data["Number of Friends"]
        c: list = test_data["Flower Cost Array"]

        expected: int = test_data["expected"]
        actual: int = get_minimum_cost_brute_force_approach(k, c)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        k: int = test_data["Number of Friends"]
        c: list = test_data["Flower Cost Array"]

        expected: int = test_data["expected"]
        actual: int = get_minimum_cost_brute_force_approach(k, c)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()
