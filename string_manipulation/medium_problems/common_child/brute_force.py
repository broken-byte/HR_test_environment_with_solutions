from tools.iterables.sub_iterables import \
    generate_all_sub_sequences_of_an_iterable
from string_manipulation.medium_problems.common_child.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def get_lcs_brute_force(s1: str, s2: str) -> int:  # Total Time Complexity = O(2^n)
    """
    Trivial brute force approach that gets all subsequences possible and compares.
    - Time Complexity: O(2^n)
    """
    sub_sequences1 = set(generate_all_sub_sequences_of_an_iterable(s1))  # O(2^n)
    sub_sequences2 = set(generate_all_sub_sequences_of_an_iterable(s2))  # O(2^n)

    common_sequences_between1_and2 = sub_sequences1.intersection(sub_sequences2)  # O(2*2^n

    lengths_of_common_sequences_between1_and2 = [len(sub) for sub in common_sequences_between1_and2]  # O(2*2^n)
    longest_common_subsequence_length = max(lengths_of_common_sequences_between1_and2)  # O(2*2^n)
    return longest_common_subsequence_length


if __name__ == "__main__":
    dynamically_generate_tests(functionality_test_data, get_lcs_brute_force, timed=True, timeout=2)
    run_dynamic_tests()
