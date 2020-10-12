from unittest import TestCase, main

from searching.hard_problems.making_candies.brute_force_making_candies import brute_force_making_candies


class BruteForceMakingCandiesTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "m": 1,
            "w": 2,
            "p": 1,
            "n": 60,
            "expected": 4
        },
        "test_1": {
            "m": 3,
            "w": 1,
            "p": 2,
            "n": 12,
            "expected": 3
        },
        "test_2": {
            "m": 1,
            "w": 1,
            "p": 6,
            "n": 45,
            "expected": 16
        },
        "test_3": {
            "m": 5184889632,
            "w": 5184889632,
            "p": 20,
            "n": 10000,
            "expected": 1
        }
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        m: int = test_data["m"]
        w: int = test_data["w"]
        p: int = test_data["p"]
        n: int = test_data["n"]

        expected: int = test_data["expected"]
        actual: int = brute_force_making_candies(m, w, p, n)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        m: int = test_data["m"]
        w: int = test_data["w"]
        p: int = test_data["p"]
        n: int = test_data["n"]

        expected: int = test_data["expected"]
        actual: int = brute_force_making_candies(m, w, p, n)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        m: int = test_data["m"]
        w: int = test_data["w"]
        p: int = test_data["p"]
        n: int = test_data["n"]

        expected: int = test_data["expected"]
        actual: int = brute_force_making_candies(m, w, p, n)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        m: int = test_data["m"]
        w: int = test_data["w"]
        p: int = test_data["p"]
        n: int = test_data["n"]

        expected: int = test_data["expected"]
        actual: int = brute_force_making_candies(m, w, p, n)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()


