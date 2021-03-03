from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from greedy_algorithms.medium_problems.max_min.test_resources.functionality_test_data import functionality_test_data
from greedy_algorithms.medium_problems.max_min.test_resources.time_complexity_test_data import time_complexity_test_data


def optimal(k: int, arr: list) -> int:
    n: int = len(arr)
    arr_sorted: list = sorted(arr)
    min_unfairness: int = get_unfairness(0, k - 1, arr_sorted)

    for index in range(n):
        sub_arr_end_index: int = index + (k - 1)
        if sub_arr_end_index < n:
            unfairness: int = get_unfairness(index, sub_arr_end_index, arr_sorted)
            if unfairness < min_unfairness:
                min_unfairness = unfairness

    return min_unfairness


def get_unfairness(index: int, sub_arr_end_index: int, arr: list) -> int:
    max_value: int = arr[sub_arr_end_index]
    min_value: int = arr[index]
    unfairness: int = max_value - min_value
    return unfairness


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
