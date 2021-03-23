from searching.medium_problems.pairs.classes.KDifferenceCounter import KDifferenceCounter
from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.pairs.test_resources.functionality_test_data import functionality_test_data
from searching.medium_problems.pairs.test_resources.time_complexity_test_data import time_complexity_test_data


def optimal(k: int, arr: list) -> int:
    k_difference_counter = KDifferenceCounter(k, arr)
    k_difference_counter.count_k_differences()
    return k_difference_counter.count


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
