from typing import List

from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from dynamic_programming.medium_problems.abbreviation.test_resources.functionality_test_data import \
    functionality_test_data
from dynamic_programming.medium_problems.abbreviation.test_resources.time_complexity_test_data import \
    time_complexity_test_data
from tools.logging.recursion import log_recursion
from tools.strings.string_transformers import capitalize_character_at, delete_character_at


def optimal_abbreviation(a: str, b: str) -> str:
    abbreviation_checker: AbbreviationChecker = AbbreviationChecker(a, b)
    if abbreviation_checker.can_make_abbreviation():
        return "YES"
    else:
        return "NO"


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
        M, N = len(self.a), len(self.b)

        for I in range(self.a_length):
            for J in range(self.b_):
                L1, L2 = self.a[I], self.b[J]
                if L1.lower() == L1:  # when lower, delete it, or capitalized it, and if capitalized, it must match.
                    self.memo[I, J] = self.dp(I - 1, J) or (self.dp(I - 1, J - 1) and L1.upper() == L2)
                else:
                    # If already capilized, then must match.
                    self.memo[I, J] = L1 == L2 and self.dp(I - 1, J - 1)

        Res = True if self.memo[M - 1, N - 1] else False
        return Res

    def dp(self, I, J):
        if (I, J) in self.memo:
            return self.memo[I, J]
        if I < 0 and J < 0:
            return True
        if I < 0:
            return False
        if J < 0:
            return True


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, optimal_abbreviation, timed=True, timeout=2)
    run_dynamic_tests()
