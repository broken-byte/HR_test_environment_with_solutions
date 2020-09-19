

class KDifferenceCounter:

    def __init__(self, k: int, arr: list):
        self.k: int = k
        self.arr: list = arr
        self.length: int = len(arr)
        self.left_cursor: int = 0
        self.right_cursor: int = 1
        self.count: int = 0

    def count_k_differences(self):
        sorted_arr: list = sorted(self.arr)
        while self.still_in_bounds():
            self.move_cursors_through_sorted_array_while_counting(sorted_arr)
        return self.count

    def still_in_bounds(self):
        return self.right_cursor < self.length

    def move_cursors_through_sorted_array_while_counting(self, sorted_arr: list):
        left: int = sorted_arr[self.left_cursor]
        right: int = sorted_arr[self.right_cursor]
        difference: int = right - left
        self.increment_given(difference)

    def increment_given(self, difference: int):
        if difference < self.k:
            self.right_cursor += 1
        elif difference == self.k:
            self.count += 1
            self.left_cursor += 1
            self.right_cursor += 1
        elif difference > self.k:
            self.left_cursor += 1
