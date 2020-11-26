from string_manipulation.easy_problems.alternating_characters.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def alternating_characters(s: str) -> int:
    min_deletions = 0
    for index in range(len(s) - 1):
        if s[index] == s[index + 1]:
            min_deletions += 1
    return min_deletions


if __name__ == "__main__":
    dynamically_generate_tests(functionality_test_data, alternating_characters)
    run_dynamic_tests()
