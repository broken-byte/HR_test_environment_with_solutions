from typing import List

from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from dynamic_programming.medium_problems.abbreviation.test_resources.functionality_test_data import \
    functionality_test_data
from dynamic_programming.medium_problems.abbreviation.test_resources.time_complexity_test_data import \
    time_complexity_test_data
from tools.logging.dynamic_programming import log_memoization_table


def optimal_abbreviation(a: str, b: str) -> str:
    abbreviation_checker: AbbreviationChecker = AbbreviationChecker(a, b)
    if abbreviation_checker.can_make_abbreviation():
        return "YES"
    else:
        return "NO"

# TODO: Need to convert the memo into a 2D Matrix, since while right it works, the hashing approach is non-intuitive,
#       And additionally logging the dictionary is severely unhelpful as the indices are the keys yet they arent lined
#       up with the actual characters in each string.


class AbbreviationChecker:
    def __init__(self, a: str, b: str):
        self.a: str = a
        self.a_length: int = len(a)
        self.b: str = b
        self.b_length: int = len(b)
        self.memo: dict = {}

    def can_make_abbreviation(self) -> bool:
        return self.search_for_abbreviation()

    def search_for_abbreviation(self):
        """
        # Complete the abbreviation function below.
        def abbreviation(a, b):
            T = {}
            M, N = len(a), len(b)
            def DP(I, J):
                if (I, J) in T:
                    return T[I, J]
                if I < 0 and J < 0:
                    return True
                if I < 0:
                    return False
                if J < 0:
                    return True

            for I in range(M):
                for J in range(N):
                    L1, L2 = a[I], b[J]
                    if L1.lower() == L1: # when lower, delete it, or capitalized it, and if capitalized, it must match.
                        T[I, J] = DP(I - 1, J) or (DP(I - 1, J - 1) and L1.upper() == L2)
                    else:
        # If already capilized, then must match.
                        T[I, J] = L1 == L2 and DP(I - 1, J - 1)

            Res = "YES" if T[M - 1, N - 1] else "NO"
            print(Res)
            return Res
        """
        self.memo = {}
        for i in range(self.a_length):
            for j in range(self.b_length):
                log_memoization_table(self.memo)
                a_letter, b_letter = self.a[i], self.b[j]
                if a_letter.islower():  # When lower, delete it, or capitalize it, & if capitalized, must match.
                    memo_key: tuple = (i, j)
                    memo_value: bool = (self.dp(i - 1, j)) or \
                                       (self.dp(i - 1, j - 1) and self.capitalization_does_match_b(a_letter, b_letter))
                    self.memoize(memo_key, memo_value)
                else:
                    # If already capitalized, then must match.
                    memo_key: tuple = (i, j)
                    memo_value: bool = (a_letter == b_letter) and \
                                       (self.dp(i - 1, j - 1))
                    self.memoize(memo_key, memo_value)
        if self.memo[self.a_length - 1, self.b_length - 1]:
            return True
        else:
            return False

    def memoize(self, key: tuple, value: bool):
        self.memo[key] = value

    @staticmethod
    def capitalization_does_match_b(a_letter: str, b_letter: str):
        return a_letter.upper() == b_letter

    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[i, j]
        if i < 0 and j < 0:
            return True
        if i < 0:
            return False
        if j < 0:
            return True


if __name__ == '__main__':
    # functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, optimal_abbreviation, timed=True)
    run_dynamic_tests()
