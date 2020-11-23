from test_utilities.dynamic_test_creation.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from test_utilities.test_variables import test_suite_separation_line
from dynamic_programming.medium_problems.abbreviation.test_resources.functionality_test_data import \
    functionality_test_data
from dynamic_programming.medium_problems.abbreviation.test_resources.time_complexity_test_data import \
    time_complexity_test_data


def optimal_abbreviations(**kwargs) -> str:
    pass


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, optimal_abbreviations)
    run_dynamic_tests()
    print(test_suite_separation_line)
    dynamically_generate_tests(time_complexity_test_data, optimal_abbreviations, timed=True, timeout=4)
    run_dynamic_tests()
