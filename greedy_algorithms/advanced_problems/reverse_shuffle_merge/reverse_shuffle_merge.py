from itertools import permutations
from collections import Counter

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.classes.StringInterLeaver import StringInterLeaver


def reverse_shuffle_merge(s):
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


def brute_force_reverse_shuffle_merge(s: str) -> str:
    # Get char counts of s
    s_counts: dict = Counter(s)
    # Get char counts that must be in A
    a_counts = {
        char: int(count / 2) for char, count in s_counts.items()
    }
    # convert a_counts into a string
    a_counts_as_string: str = ""
    for char, count in a_counts.items():
        for _ in range(count):
            a_counts_as_string += char

    # get all permutations of a_counts_as_string
    permutations_of_a: list = list(permutations(a_counts_as_string, len(a_counts_as_string)))
    string_permutations_of_a: list = ["".join(permutation) for permutation in permutations_of_a]
    # Get the minimum
    lexigraphically_smallest_a: str = min(string_permutations_of_a)
    return lexigraphically_smallest_a


def reverse(a: str) -> str:
    return a[::-1]


def shuffle(a: str) -> list:
    permutations_of_a: list = list(permutations(a, len(a)))
    permutations_of_a: list = ["".join(permutation) for permutation in permutations_of_a]
    return permutations_of_a


def merge(a1: str, a2: str) -> list:
    inter_leaver: StringInterLeaver = StringInterLeaver(a1, a2)
    return inter_leaver.get_all_possible_inter_leaves()


def get_all_possible_string_bisections(s: str) -> list:
    length_of_s: int = len(s)
    bisections: list = []

    for index in range(length_of_s):
        left: str = s[:index]
        right: str = s[index:]
        bisection: list = [left, right]
        if len(left) != 0 and len(right) != 0:
            bisections.append(bisection)

    return bisections


def get_bisections(s: str) -> tuple:
    middle_index: int = int(len(s) / 2)
    left: str = s[:middle_index]
    right: str = s[middle_index:]
    return left, right


def main():
    brute_force_reverse_shuffle_merge("eggegg")


if __name__ == "__main__":
    main()


