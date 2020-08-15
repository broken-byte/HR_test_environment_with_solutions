from itertools import permutations

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.classes.StringInterLeaver import StringInterLeaver

# TODO: Create a valid A checker function test, THEN create a valid A checker

def brute_force_reverse_shuffle_merge(s: str) -> str:
    # Bisection of s
    bisection: tuple = get_bisections(s)
    # Path 1:
    s_1: str = bisection[0]
    s_2: str = bisection[1]
    a_1: str = reverse(s_1)
    a_2: str = reverse(s_2)
    print(a_1, shuffle(a_1))
    print(a_2, shuffle(a_2))


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
    print(shuffle("egg"))


if __name__ == "__main__":
    main()


