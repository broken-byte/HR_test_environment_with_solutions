import bisect


def optimized_triple_sum(a: list, b: list, c: list) -> int:  #O(b*[log(a) + log(c)])
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    count: int = 0
    if a[0] > b[-1] or b[-1] < c[0]:
        return 0
    for q in b:  # O(b)
        index_of_q_in_a: int = bisect.bisect_right(a, q)  # O(log(a)
        index_of_q_in_c: int = bisect.bisect_right(c, q)  # O(log(c)
        if index_of_q_in_a != 0 and index_of_q_in_c != 0:
            count += index_of_q_in_a * index_of_q_in_c
    return count


