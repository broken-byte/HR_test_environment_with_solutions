from sorting.hard_problems.count_inversions.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def count_inversions(arr: list) -> int:
    """
    Given an array of numbers, returns the number
    of inversions within the array.
        - Time Complexity: O(N*log(N))
    """
    inversion_counter: InversionCounter = InversionCounter()
    inversion_count = inversion_counter.get_inversion_count(arr)

    return inversion_count


class InversionCounter:
    """
    The solution to this problem in class form along
    with an implementation of the regular mergesort
    function that I used to guide my intuition of the 
    inversion count function
    """
    def __init__(self):
        self.inversion_count: int = 0

    def get_inversion_count(self, array: list) -> int:
        print(f"Starting array: {array}")
        sorted_array, inversion_count = self.sort_and_count(array)
        print(f"sorted array: {sorted_array}")
        return inversion_count

    def merge_sort(self, array: list) -> list:
        # Base Case
        if len(array) <= 1:
            return array
        # Recursive Case
        middle = int(len(array)/2)
        left = self.merge_sort(array[:middle])
        right = self.merge_sort(array[middle:])
        return self.merge(left, right)

    @staticmethod
    def merge(left_array: list, right_array: list) -> list:
        print(f"\nMerging left array: {left_array} with right array: {right_array}\n")
        merged_array = []  # Final output array
        left_length = len(left_array)
        right_length = len(right_array)
        left_cursor = 0
        right_cursor = 0

        while left_cursor < left_length and right_cursor < right_length:

            if left_array[left_cursor] < right_array[right_cursor]:
                merged_array.append(left_array[left_cursor])
                left_cursor += 1
            else:
                merged_array.append(right_array[right_cursor])
                right_cursor += 1
            
            print(f"Merged Array so far: {merged_array}\n")
        if left_cursor == left_length:
            merged_array.extend(right_array[right_cursor:])
        else:
            merged_array.extend(left_array[left_cursor:])
        print(f"merged: {merged_array}")
        return merged_array

    def sort_and_count(self, array: list) -> tuple:
        """"
        Given an array of numbers, returns the sorted
        array as well as the number of inversions within 
        the array.
            - Time Complexity: O(N*log(N))
        """
        inversion_count = 0
        # Base Case
        if len(array) <= 1:
            return array, inversion_count

        # Recursive Case
        middle = int(len(array)/2)

        left_array, left_inversion_count = self.sort_and_count(array[:middle])
        right_array, right_inversion_count = self.sort_and_count(array[middle:])

        merged_array, merged_inversion_count = self.merge_and_count(left_array, right_array)

        print(f"Left: {left_array}, Right: {right_array}, merged: {merged_array}")
        print(f"left inversions: {left_inversion_count}, right inversions: {right_inversion_count}, merged Inversions: {merged_inversion_count}")
        
        total_inversion_count = left_inversion_count + right_inversion_count + merged_inversion_count

        print(f"Total inversions: {total_inversion_count}")

        return merged_array, total_inversion_count

    @staticmethod
    def merge_and_count(left_array: list, right_array: list) -> tuple:
        """
        Given two sorted arrays, knits them together in sorted 
        order and returns as one unified list along with the inversion count
        """
        print(f"\nMerging left array: {left_array} with right array: {right_array}\n")

        merged_array = [] # Final ouput array
        left_length = len(left_array)
        right_length = len(right_array)
        left_cursor = 0
        right_cursor = 0
        merged_inversion_count = 0

        while left_cursor < left_length and right_cursor < right_length:

            if left_array[left_cursor] <= right_array[right_cursor]:
                merged_array.append(left_array[left_cursor])
                left_cursor += 1
            else:
                merged_array.append(right_array[right_cursor])
                merged_inversion_count += len(left_array[left_cursor:])
                right_cursor += 1

            print(f"Merged Array so far: {merged_array}\n")
        if left_cursor == left_length:
            merged_array.extend(right_array[right_cursor:])
        else:
            merged_array.extend(left_array[left_cursor:])
        print(f"merged: {merged_array}")
        print(f"Number of inversions in this merge: {merged_inversion_count}")
        return merged_array, merged_inversion_count


if __name__ == "__main__":
    dynamically_generate_tests(functionality_test_data, count_inversions)
    run_dynamic_tests()
