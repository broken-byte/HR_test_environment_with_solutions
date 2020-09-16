
# TODO: Optimize
def pairs_brute_force(k: int, arr: list) -> int:
    length: int = len(arr)
    count: int = 0
    ledger: set = set({})
    for i in range(length):
        for j in range(length):
            left: int = arr[i]
            right: int = arr[j]
            pair: tuple = tuple(sorted([str(left), str(right)]))
            if pair in ledger:
                continue
            ledger.add(pair)
            if abs(left - right) == k:
                count += 1
    return count
