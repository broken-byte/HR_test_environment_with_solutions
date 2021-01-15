from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.pairs.test_resources.functionality_test_data import functionality_test_data


def pairs(k: int, arr: list) -> int:
    # Time Complexity: O(n^2)
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


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, pairs)
    run_dynamic_tests()
