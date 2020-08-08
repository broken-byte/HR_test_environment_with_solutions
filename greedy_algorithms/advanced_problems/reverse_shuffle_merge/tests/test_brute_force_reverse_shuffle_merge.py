from unittest import TestCase, main
import os

from ..reverse_shuffle_merge import brute_force_reverse_shuffle_merge

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForceReverseShuffleMergeTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "s": "abab",
            "expected": "ab"
        },
        "test_1": {
            "s": "eggegg",
            "expected": "egg"
        },
        "test_2": {
            "s": "abcdefgabcdefg",
            "expected": "agfedcb"
        },
        "test_3": {
            "s": "aeiouuoiea",
            "expected": "aeiou"
        },
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        s: int = test_data["s"]

        expected: int = test_data["expected"]
        actual: str = brute_force_reverse_shuffle_merge(s)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        s: int = test_data["s"]

        expected: int = test_data["expected"]
        actual: str = brute_force_reverse_shuffle_merge(s)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        s: int = test_data["s"]

        expected: int = test_data["expected"]
        actual: str = brute_force_reverse_shuffle_merge(s)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        s: int = test_data["s"]

        expected: int = test_data["expected"]
        actual: str = brute_force_reverse_shuffle_merge(s)

        print(test_data, actual, "\n")
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()
