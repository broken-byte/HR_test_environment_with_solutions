from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from dynamic_programming.medium_problems.max_array_sum.test_resources.functionality_test_data import \
    functionality_test_data


def optimal_max_array_sum(**kwargs) -> int:
    arr: list = kwargs["arr"]
    maximum_sums: dict = {
        0: arr[0],
        1: max(arr[0], arr[1])
    }
    for index, number in enumerate(arr[2:], start=2):
        current_value: int = number
        maximum_sum_found_so_far: int = maximum_sums[index - 1]
        max_non_adjacent_subsequence_sum: int = maximum_sums[index - 2] + number
        maximum_sums[index]: int = max(
            current_value,
            maximum_sum_found_so_far,
            max_non_adjacent_subsequence_sum
        )
    last_index: int = len(arr) - 1
    maximum_non_adjacent_sub_sequence: int = maximum_sums[last_index]
    return maximum_non_adjacent_sub_sequence


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, optimal_max_array_sum)
    run_dynamic_tests()
