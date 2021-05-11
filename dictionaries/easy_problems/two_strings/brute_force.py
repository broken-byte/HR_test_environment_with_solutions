from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from dictionaries.easy_problems.two_strings.test_resources.functionality_test_data import functionality_test_data


def brute_force(s1: str, s2: str) -> str:
    string_1_set = set(s1)
    string_2_set = set(s2)
    common_sub_string = string_1_set.intersection(string_2_set)
    return "YES" if len(common_sub_string) != 0 else "NO"


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
