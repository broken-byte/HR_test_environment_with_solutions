

def pairs_brute_force(k: int, arr: list) -> int:
    length: int = len(arr)
    count: int = 0
    ledger: set = set({})
    for i in range(length):
        for j in range(length):
            if i + j in ledger:
                continue
            ledger.add(i + j)
            left: int = arr[i]
            right: int = arr[j]
            if abs(left - right) == k:
                count += 1
    return count
