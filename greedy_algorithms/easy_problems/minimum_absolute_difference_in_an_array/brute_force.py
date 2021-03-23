from itertools import combinations

from greedy_algorithms.easy_problems.minimum_absolute_difference_in_an_array.test_resources.functionality_test_data \
    import functionality_test_data
from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def brute_force(arr: list) -> int:
    """Time Complexity: O(n^2)"""
    all_possible_pairs = combinations(arr, 2)
    absolute_difference_of_every_pair = [abs(a[0] - a[1]) for a in all_possible_pairs]
    min_absolute_difference = min(absolute_difference_of_every_pair)
    return min_absolute_difference


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
