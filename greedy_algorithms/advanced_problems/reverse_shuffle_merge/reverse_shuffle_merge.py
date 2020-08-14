from itertools import permutations

from greedy_algorithms.advanced_problems.reverse_shuffle_merge.classes.StringInterLeaver import StringInterLeaver


def brute_force_reverse_shuffle_merge(s: str) -> str:
    pass


def reverse(a: str) -> str:
    return a[::-1]


def shuffle(a: str) -> list:
    permutations_of_a: list = list(permutations(a, len(a)))
    permutations_of_a: list = ["".join(permutation) for permutation in permutations_of_a]
    return permutations_of_a


def merge(a1: str, a2: str) -> list:
    inter_leaver: StringInterLeaver = StringInterLeaver(a1, a2)
    return inter_leaver.get_all_possible_inter_leaves()


def main():
    pass


if __name__ == "__main__":
    main()


