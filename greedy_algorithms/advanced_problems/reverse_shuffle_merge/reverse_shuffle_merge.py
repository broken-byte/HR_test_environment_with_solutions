from itertools import permutations


def brute_force_reverse_shuffle_merge(s: str) -> str:
    pass


def reverse(a: str) -> str:
    return a[::-1]


def shuffle(a: str) -> list:
    permutations_of_a: list = list(permutations(a, len(a)))
    return permutations_of_a


def merge(a1: str, a2: str) -> list:
    pass
