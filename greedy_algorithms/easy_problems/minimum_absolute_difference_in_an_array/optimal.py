from greedy_algorithms.easy_problems.minimum_absolute_difference_in_an_array.test_resources.functionality_test_data \
    import functionality_test_data
from greedy_algorithms.easy_problems.minimum_absolute_difference_in_an_array.test_resources.time_complexity_test_data \
    import time_complexity_test_data
from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def optimal(arr: list) -> int:
    """Time Complexity: O(n)"""
    n: int = len(arr)
    sorted_arr: list = sorted(arr)
    min_absolute_difference: int = abs(sorted_arr[0] - sorted_arr[1])

    for index in range(n - 1):
        absolute_difference: int = abs(sorted_arr[index] - sorted_arr[index + 1])
        if absolute_difference < min_absolute_difference:
            min_absolute_difference = absolute_difference

    return min_absolute_difference


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
