from string_manipulation.easy_problems.making_anagrams.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def making_anagrams(a: str, b: str) -> int:
    count_of_deletions_needed = 0
    unique_characters_in_both = set(a + b)
    counter_a = custom_counter(unique_characters_in_both, a)
    counter_b = custom_counter(unique_characters_in_both, b)
    for character in unique_characters_in_both:
        count_of_deletions_needed += abs(counter_a[character] - counter_b[character])
    return count_of_deletions_needed


def custom_counter(unique_characters: set, string: str) -> dict:
    """
    Given a set of all the unique instances of  different characters
    in a string and said string, returns an instance counter dictionary 
    """
    counter = {}
    for character in unique_characters:
        if character in string:
            count = 0
            for char in string:
                if character == char:
                    count += 1
            counter[character] = count
        else:
            counter[character] = 0
    return counter


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, making_anagrams)
    run_dynamic_tests()
