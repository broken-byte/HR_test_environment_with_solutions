from unittest import TestCase, main

from searching.medium_problems.ice_cream_parlor.optimized import what_flavors
from searching.medium_problems.ice_cream_parlor.tests.BruteForceTester import BruteForceTester


class OptimizedTester(TestCase):

    functionality_test_data: dict = BruteForceTester.functionality_test_data

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        trips: list = test_data["trips"]

        expected: list = test_data["expected"]
        actual: list = what_flavors(trips)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        trips: list = test_data["trips"]

        expected: list = test_data["expected"]
        actual: list = what_flavors(trips)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        trips: list = test_data["trips"]

        expected: list = test_data["expected"]
        actual: list = what_flavors(trips)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        trips: list = test_data["trips"]

        expected: list = test_data["expected"]
        actual: list = what_flavors(trips)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


