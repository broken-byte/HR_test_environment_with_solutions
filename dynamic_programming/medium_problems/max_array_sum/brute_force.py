import logging


logging.basicConfig(level=logging.DEBUG)


def max_subset_sum(arr: list) -> int:
    dp = {}  # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        logging.debug(f"dynamic programming dp: {dp}")
        dp[i] = max(dp[i - 1], dp[i - 2] + num, dp[i - 2], num)
    return dp[len(arr) - 1]

# TODO: Analyze the above solution and make your own


class SubSequenceGenerator:
    def __init__(self, array: list):
        self.array: list = array
        self.non_adjacent_sub_sequences: list = []
        self.sub_sequences: list = []

    def get_all_non_adjacent_sub_sequences(self) -> list:
        self.recursively_build_non_adjacent_sub_sequences([], -1, 0)
        return self.non_adjacent_sub_sequences

    def get_all_sub_sequences(self):
        self.recursively_build_sub_sequences([], 0)
        return self.sub_sequences

    def recursively_build_non_adjacent_sub_sequences(self, sub: list, previously_added_i: int, current_i: int):
        if current_i == len(self.array):
            if len(sub) != 0:
                self.sub_sequences.append(sub)
        else:
            # traverse without adding
            self.recursively_build_non_adjacent_sub_sequences(sub, previously_added_i, current_i + 1)

            if current_i == 0:  # Add first time only
                self.recursively_build_non_adjacent_sub_sequences(sub + [self.array[current_i]], current_i,
                                                                  current_i + 1)
            elif current_i - previously_added_i > 1:  # Add if difference is greater than 1
                self.recursively_build_non_adjacent_sub_sequences(sub + [self.array[current_i]], current_i,
                                                                  current_i + 1)
            else:  # traverse without adding
                self.recursively_build_non_adjacent_sub_sequences(sub, current_i, current_i + 1)

    def recursively_build_sub_sequences(self, sub: list, current_i):
        if current_i == len(self.array):
            if len(sub) != 0:
                self.sub_sequences.append(sub)
        else:
            # Omit
            self.recursively_build_sub_sequences(sub, current_i + 1)
            # Add
            self.recursively_build_sub_sequences(sub + [self.array[current_i]], current_i + 1)


if __name__ == '__main__':
    max_subset_sum([-2, 1, 3])
