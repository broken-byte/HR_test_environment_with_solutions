from itertools import combinations


def minimum_absolute_difference(arr: list) -> int:
    """
    Houses algorithm to be tested for time complexity and final solution
    Current algorithm being housed:
        - minimumAbsoluteDifferenceOptimized0(arr: list) -> int
    """
    n: int = len(arr)
    sorted_arr: list = sorted(arr)
    min_absolute_difference: int = abs(sorted_arr[0] - sorted_arr[1])

    for index in range(n - 1):
        absolute_difference: int = abs(sorted_arr[index] - sorted_arr[index + 1])
        if absolute_difference < min_absolute_difference:
            min_absolute_difference = absolute_difference

    return min_absolute_difference


def minimum_absolute_difference_brute_force(arr: list) -> int:
    """Time Complexity: O(n^2)"""
    all_possible_pairs = combinations(arr, 2)
    absolute_difference_of_every_pair = [abs(a[0] - a[1]) for a in all_possible_pairs]
    min_absolute_difference = min(absolute_difference_of_every_pair)
    return min_absolute_difference


def minimum_absolute_difference_optimized(arr: list) -> int:
    """Time Complexity: O(n)"""
    n: int = len(arr)
    sorted_arr: list = sorted(arr)
    min_absolute_difference: int = abs(sorted_arr[0] - sorted_arr[1])

    for index in range(n - 1):
        absolute_difference: int = abs(sorted_arr[index] - sorted_arr[index + 1])
        if absolute_difference < min_absolute_difference:
            min_absolute_difference = absolute_difference

    return min_absolute_difference


if __name__ == "__main__":
    pass
