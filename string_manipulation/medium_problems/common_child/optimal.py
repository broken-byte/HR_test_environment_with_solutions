from string_manipulation.medium_problems.common_child.test_resources.functionality_test_data import \
    functionality_test_data
from string_manipulation.medium_problems.common_child.test_resources.time_complexity_test_data import \
    time_complexity_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def common_child(s1: str, s2: str) -> int:
    """
    The implementation that will ultimately be submitted to
    HackerRank for evaluation, using the most optimal algorithm
    in this file!
    Current implementation: get_lcs_memoized_iterative_approach()
    """
    n = len(s1)
    m = len(s2)
    memo = [[0] * (n + 1) for _ in range(m + 2)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
            else:
                comparison1 = memo[i + 1][j]
                comparison2 = memo[i][j + 1]
                memo[i + 1][j + 1] = max(comparison1, comparison2)
    return memo[n][m]


def get_lcs_memoized_iterative_approach(s1: str, s2: str) -> int: # O(n*m)
    """
    Dynamic Programming approach utilizing a 2D memo array but using iteration
    vs. recursion to solve a stack limit issue with VSCode.
        - Time Complexity: O(n*m)
    """
    n = len(s1)
    m = len(s2)
    memo = [[0]* (n + 1) for _ in range(m + 2)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
            else:
                comparison1 = memo[i + 1][j]
                comparison2 = memo[i][j + 1]
                memo[i + 1][j + 1] = max(comparison1, comparison2)
    return memo[n][m]


def get_lcs_memoized_approach(s1: str, s2: str) -> int: # Total Time Complexity = O(n*m)
    """
    Recursive bottom up approach that utilizes a 2D memo array, optimizes from O(2^n) -> O(n*m).
    - Time Complexity: O(N*m)
    """
    n = len(s1)
    m = len(s2)
    memo = [[None for _ in range(m)] for _ in range(n)]

    def longest_common_subsequence_generator(i: int , j: int) -> int:  # O(n*m)
        # Recursive driver function for LCS
        if i == len(s1) or j == len(s2): # Base Case
            return 0
        elif memo[i][j] is not None:  # Memoized Case
            return memo[i][j]
        elif s1[i] == s2[j]:
            result = 1 + longest_common_subsequence_generator(i + 1, j + 1)
        elif s1[i] != s2[j]:
            comparison1 = longest_common_subsequence_generator(i + 1, j)
            comparison2 = longest_common_subsequence_generator(i, j + 1)
            result = max(comparison1, comparison2)
        memo[i][j] = result
        return result

    lcs_length = longest_common_subsequence_generator(0, 0)
    return lcs_length


def get_lcs_bottom_up(s1: str, s2: str) -> int:
    """
    Bottom up recursive approach that starts from indices 0, 0
    - Time Complexity: O(2^n)
    """
    n, m = len(s1), len(s2)

    def longest_common_sub_sequence_generator(s_1: str, s_2: str, i: int, j: int) -> int:
        # Recursive driver function for LCS
        if i == n or j == m:  # Base Case
            result = 0
        elif s_1[i] == s_2[j]:
            result = 1 + longest_common_sub_sequence_generator(s_1, s_2, i + 1, j + 1)
        elif s_1[i] != s_2[j]:
            comparison1 = longest_common_sub_sequence_generator(s_1, s_2, i + 1, j)
            comparison2 = longest_common_sub_sequence_generator(s_1, s_2, i, j + 1)
            result = max(comparison1, comparison2)
        return result

    lcs_length = longest_common_sub_sequence_generator(s1, s2, 0, 0)
    return lcs_length


def get_lcs_backward_approach(s1: str, s2: str)-> int:
    """
    Backward recursive approach that starts at the ends of the strings
    - Time Complexity: O(2^n)
    """
    n, m = len(s1), len(s2)

    def longest_common_subsequence_generator(s_1: str, s_2: str, i: int, j: int) -> int:  # O(2^(n + m)
        # Recursive driver function for LCS
        if i == 0 or j == 0:  # Base Case
            result = 0
        elif s_1[i - 1] == s_2[j - 1]:  # Matching Recursive Case
            result = 1 + longest_common_subsequence_generator(s_1, s_2, i - 1, j - 1)
        elif s_1[i - 1] != s_2[j - 1]:  # Different Recursive Case
            temp1 = longest_common_subsequence_generator(s_1, s_2, i - 1, j)
            temp2 = longest_common_subsequence_generator(s_1, s_2, i, j - 1)
            result = max(temp1, temp2)
        return result

    lcs_length = longest_common_subsequence_generator(s1, s2, n, m)
    return lcs_length


if __name__ == "__main__":
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, common_child, timed=True, timeout=15)
    run_dynamic_tests()
