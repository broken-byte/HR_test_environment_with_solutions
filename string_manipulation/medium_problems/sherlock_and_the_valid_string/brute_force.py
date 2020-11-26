import string 
import random

from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from string_manipulation.medium_problems.sherlock_and_the_valid_string.test_resources.functionality_test_data import \
    functionality_test_data


def is_valid(**kwargs) -> str:
    s: int = kwargs["s"]
    frequency_of_distinct_characters_in_string = [s.count(letter) for letter in set(s) ]
    highest_count = max(frequency_of_distinct_characters_in_string)
    lowest_count = min(frequency_of_distinct_characters_in_string)
    if highest_count - lowest_count == 0:  # If all values equal, return 'YES'
        return 'YES'
    # If difference between highest count and lowest count is 1
    # and there is only one letter with highest count,
    # then return 'YES' (because we can subtract one of these
    # letters and max=min , i.e. all counts are the same)
    elif (frequency_of_distinct_characters_in_string.count(highest_count) == 1 and
          highest_count - lowest_count) == 1:
        return 'YES'

    # If the minimum count is 1
    # then remove this letter, and check whether all the other
    # counts are the same
    elif frequency_of_distinct_characters_in_string.count(lowest_count) == 1:
        frequency_of_distinct_characters_in_string.remove(lowest_count)
        # Recalculate 
        highest_count = max(frequency_of_distinct_characters_in_string)
        lowest_count = min(frequency_of_distinct_characters_in_string)
        # Check
        if highest_count - lowest_count == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


def generate_random_string() -> str:
    random_string = ''.join(random.choices(string.ascii_lowercase, k=7))
    return random_string


if __name__ == "__main__":
    dynamically_generate_tests(functionality_test_data, is_valid, timed=True, timeout=2)
    run_dynamic_tests()
