from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from string_manipulation.medium_problems.special_string_again.test_resources.functionality_test_data import \
    functionality_test_data
from tools.iterables.sub_iterables import \
    number_of_sub_arrays_in_an_iterable


def substr_count_slow(n: int, s: str) -> int: # O(n^2)
    """
    Works reliably and simple to understand
    but does not meet the runtime complexity
    requirements of the hackerank test
        Time Complexity: O(N^2)
    """
    if all_chars_equal(s):
        return number_of_sub_arrays_in_an_iterable(n)  # Efficient for all equal case
    sub_strings = get_sub_strings_greater_than_length_one(n, s)  # O(n^2)
    special_string_count = n
    for sub in sub_strings:  # ~= O(n)* O(n) = O(n^2)
        if is_special(sub):
            special_string_count += 1
    return special_string_count


def get_sub_strings_greater_than_length_one(n: int, s: str) -> list:  # O(n^2)
    sub_strings = []
    for i in range(n):
        sub=""
        for j in range(i,n):
            sub += s[j]
            if len(sub) != 1: sub_strings.append(sub)
    return sub_strings


def is_special(sub_string: str) -> bool:  # O(n) + O(n) <= O(n)
    if all_chars_equal(sub_string):
        return True
    elif all_chars_except_middle_equal(sub_string):
        return True
    else:
        return False


def all_chars_equal(s: str) -> bool: # O(n)
    if s == len(s) * s[0]:
        return True


def all_chars_except_middle_equal(s: str) -> bool: # O(n)
    n = len(s)
    if n % 2 == 0: return False  # Even strings have no middle
    middle = int(n / 2)
    s = s[:middle] + s[middle + 1:]
    if all_chars_equal(s): return True


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, substr_count_slow)
    run_dynamic_tests()
