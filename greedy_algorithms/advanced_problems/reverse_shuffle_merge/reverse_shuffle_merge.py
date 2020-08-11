from itertools import permutations
import itertools


def brute_force_reverse_shuffle_merge(s: str) -> str:
    pass


def reverse(a: str) -> str:
    return a[::-1]


def shuffle(a: str) -> list:
    permutations_of_a: list = list(permutations(a, len(a)))
    return permutations_of_a


def merge(a1: str, a2: str) -> list:
    pass


def in_order_combinations(*lists):
    lists = list(filter(len, lists))

    if len(lists) == 0:
        yield []

    for lst in lists:
        element = lst.pop()
        for combination in in_order_combinations(*lists):
            yield combination + [element]
        lst.append(element)


if __name__ == "__main__":
    for combo in in_order_combinations(['a', 'b'], [1, 2, 3]):
        print(''.join(map(str, combo)))
