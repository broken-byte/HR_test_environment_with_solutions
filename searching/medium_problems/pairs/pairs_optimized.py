from searching.medium_problems.pairs.classes.KDifferenceCounter import KDifferenceCounter


def pairs_optimized(k: int, arr: list) -> int:
    k_difference_counter = KDifferenceCounter(k, arr)
    k_difference_counter.count_k_differences()
    return k_difference_counter.count
