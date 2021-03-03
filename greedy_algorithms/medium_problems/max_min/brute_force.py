from itertools import combinations

from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from greedy_algorithms.medium_problems.max_min.test_resources.functionality_test_data import functionality_test_data


def brute_force(k: int, arr: list) -> int:
    all_k_combinations_of_arr = combinations(arr, k)
    all_k_combinations_of_arr = list(all_k_combinations_of_arr)
    min_unfairness: int = max(all_k_combinations_of_arr[0]) - min(all_k_combinations_of_arr[0])
    for combination in all_k_combinations_of_arr:
        unfairness: int = max(combination) - min(combination)
        if unfairness < min_unfairness:
            min_unfairness = unfairness
    return min_unfairness


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
