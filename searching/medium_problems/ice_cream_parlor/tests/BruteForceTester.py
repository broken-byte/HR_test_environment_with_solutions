from unittest import TestCase, main

from searching.medium_problems.ice_cream_parlor.brute_force import what_flavors


class BruteForceTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "trips": [
                {
                    "money": 5,
                    "cost": [2, 1, 3, 5, 6]
                }
            ],
            "expected": [
                [1, 3]
            ]
        },
        "test_1": {
            "trips": [
                {
                    "money": 4,
                    "cost": [1, 4, 5, 3, 2]
                },
                {
                    "money": 4,
                    "cost": [2, 2, 4, 3]
                }
            ],
            "expected": [
                [1, 4],
                [1, 2]
            ]
        },
        "test_2": {
            "trips": [
                {
                    "money": 5,
                    "cost": [1, 2, 3, 5, 6]
                }
            ],
            "expected": [
                [2, 3]
            ]
        },
        "test_3": {
            "trips": [
                {
                    "money": 8,
                    "cost": [4, 3, 2, 5, 7]
                },
                {
                    "money": 12,
                    "cost": [7, 2, 5, 4, 11]
                }
            ],
            "expected": [
                [2, 4],
                [1, 3]
            ]
        }
    }

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


