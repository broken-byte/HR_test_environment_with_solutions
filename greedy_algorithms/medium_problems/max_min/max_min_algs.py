from itertools import combinations


def max_min_brute_force_approach(k: int, arr: list) -> int:
    all_k_combinations_of_arr = combinations(arr, k)
    all_k_combinations_of_arr = list(all_k_combinations_of_arr)
    min_unfairness: int = max(all_k_combinations_of_arr[0]) - min(all_k_combinations_of_arr[0])
    for combination in all_k_combinations_of_arr:
        unfairness: int = max(combination) - min(combination)
        if unfairness < min_unfairness:
            min_unfairness = unfairness
    return min_unfairness


def max_min_optimized(k: int, arr: list) -> int:
    n: int = len(arr)
    arr_sorted: list = sorted(arr)
    min_unfairness: int = get_unfairness(0, k - 1, arr_sorted)

    for index in range(n):
        sub_arr_end_index: int = index + (k - 1)
        if sub_arr_end_index < n:
            unfairness: int = get_unfairness(index, sub_arr_end_index, arr_sorted)
            if unfairness < min_unfairness:
                min_unfairness = unfairness

    return min_unfairness


def get_unfairness(index: int, sub_arr_end_index: int, arr: list) -> int:
    max_value: int = arr[sub_arr_end_index]
    min_value: int = arr[index]
    unfairness: int = max_value - min_value
    return unfairness
