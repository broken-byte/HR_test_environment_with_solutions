from unittest import TestCase, main
import os

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.reverse_shuffle_merge import reverse, shuffle, merge

current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class HelperFunctionTester(TestCase):

    def test_reverse(self):
        expected: str = "cba"
        actual: str = reverse("abc")
        self.assertEqual(expected, actual)

    def test_shuffle(self):
        expected: list = ['god', 'gdo', 'ogd', 'odg', 'dgo', 'dog']
        actual: list = shuffle("god")
        self.assertEqual(expected, actual)

    def test_merge(self):
        expected: list = ['123ab', '12a3b', '12ab3', '1a23b', '1a2b3', '1ab23', 'a123b', 'a12b3', 'a1b23', 'ab123']
        actual: list = merge("123", "ab")
        self.assertEqual(expected, actual)
