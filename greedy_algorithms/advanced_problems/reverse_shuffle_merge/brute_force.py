from itertools import permutations
from collections import Counter

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, \
    run_dynamic_tests


def brute_force(s: str) -> str:
    # Get char counts of s
    s_counts: dict = Counter(s)
    # Get char counts that must be in A
    a_counts = {
        char: int(count / 2) for char, count in s_counts.items()
    }
    # convert a_counts into a string
    a_counts_as_string: str = ""
    for char, count in a_counts.items():
        for _ in range(count):
            a_counts_as_string += char

    # get all permutations of a_counts_as_string
    permutations_of_a: list = list(permutations(a_counts_as_string, len(a_counts_as_string)))
    string_permutations_of_a: list = ["".join(permutation) for permutation in permutations_of_a]
    # Get the minimum
    lexigraphically_smallest_a: str = min(string_permutations_of_a)
    return lexigraphically_smallest_a


if __name__ == "__main__":
    print(functionality_test_data)
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
