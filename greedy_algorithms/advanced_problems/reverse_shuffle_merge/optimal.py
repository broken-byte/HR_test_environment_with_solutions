from collections import Counter

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, \
    run_dynamic_tests


def optimal(s):
    char_count = Counter(s)
    string_chars = {
        char: int(count / 2) for char, count in char_count.items()
    }
    shuffled_chars = {
        char: int(count / 2) for char, count in char_count.items()
    }
    result_string: list = []

    for char in reversed(s):
        current_char_count: int = string_chars[char]

        if character_count_not_empty(current_char_count):

            while (string_not_empty(result_string) and
                   character_is_lexigraphically_larger(result_string[-1], char) and
                   character_count_not_empty(shuffled_chars[result_string[-1]])):

                removed = result_string.pop()
                string_chars[removed] += 1
                shuffled_chars[removed] -= 1

            result_string.append(char)
            string_chars[char] -= 1
        else:
            shuffled_chars[char] -= 1

    return ''.join(result_string)


def character_count_not_empty(char_count: int) -> bool:
    return char_count > 0


def character_is_lexigraphically_larger(char1: str, char2: str) -> bool:
    return char1 > char2


def string_not_empty(string: list) -> bool:
    return len(string) > 0


if __name__ == "__main__":
    print(functionality_test_data)
    dynamically_generate_tests(functionality_test_data, optimal)
    run_dynamic_tests()
