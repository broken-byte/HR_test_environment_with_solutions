from unittest import TestCase, skip, main

from .greedy_florist_algs import get_minimum_cost_brute_force_approach
from test_utilities.test_variables import console_break_line


class GreedyFloristAlgsTester(TestCase):

    functionalityTests: dict = {
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
        
    def testBruteForceApproach(self):
        print("\nBrute Force Functionality Tests\n", console_break_line)
        for testName, testData in self.functionalityTests.items():
            try:
                k: int = testData["Number of Friends"]
                c: list = testData["Flower Cost Array"]
                expected: int = testData["expected"]
                actual: int = get_minimum_cost_brute_force_approach(k, c)
                print(testName, testData, actual, "\n")
                self.assertEqual(expected, actual)

            except AssertionError as error:
                print(error)


if __name__ == "__main__":
    main()
