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
    inversion_count = sort_and_count(arr)

    return inversion_count[1]


def sort_and_count(array: list) -> tuple:
    """
    Recursive modified mergesort that counts
    inversions while sorting
    """
    inversion_count = 0
    array_length = len(array)

    # Base Case
    if array_length <= 1:
        return array, inversion_count

    # Recursive Case
    middle = int(array_length/2)

    left_array, left_inversion_count = sort_and_count(array[:middle])
    right_array, right_inversion_count = sort_and_count(array[middle:])

    merged_array, merged_inversion_count = merge_and_count(left_array, right_array)
    total_inversion_count = left_inversion_count + right_inversion_count + merged_inversion_count

    return merged_array, total_inversion_count


def merge_and_count(left_array: list, right_array: list) -> tuple:
    """
    Given two sorted arrays, knits them together in sorted 
    order and returns as one unified list along with the inversion count
    """
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
            merged_inversion_count += left_length - left_cursor
            right_cursor += 1
    if left_cursor == left_length:
        merged_array.extend(right_array[right_cursor:])
    else:
        merged_array.extend(left_array[left_cursor:])
    return merged_array, merged_inversion_count

   
if __name__ == "__main__":
    dynamically_generate_tests(functionality_test_data, count_inversions)
    run_dynamic_tests()

