from unittest import TestCase, main
import os

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.reverse_shuffle_merge import reverse
from greedy_algorithms.advanced_problems.reverse_shuffle_merge.reverse_shuffle_merge import shuffle
from greedy_algorithms.advanced_problems.reverse_shuffle_merge.reverse_shuffle_merge import merge
from greedy_algorithms.advanced_problems.reverse_shuffle_merge.reverse_shuffle_merge import get_all_possible_string_bisections
from greedy_algorithms.advanced_problems.reverse_shuffle_merge.reverse_shuffle_merge import get_bisections

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

    def test_all_possible_string_bisections(self):
        expected: list = [["a", "bc"], ["ab", "c"]]
        actual: list = get_all_possible_string_bisections("abc")
        self.assertEqual(expected, actual)

    def test_get_bisection(self):
        expected: tuple = ('egg', 'egg')
        actual: tuple = get_bisections('eggegg')
        self.assertEqual(expected, actual)

