

def get_number_of_sub_arrays_in_an_iterable(n: int) -> int:
    """
    Returns the number of sub arrays
    (consecutive, adjacent elements) in an iterable
    given the number of elements.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return int((n**2 + n) / 2)


def generate_all_sub_sequences_of_an_iterable(iterable) -> list:
    """
    Recursively generate all subsequences (contiguous or non contiguous elements) of an iterable
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    n = len(iterable)
    sub_sequences = []

    def recursive_sub_sequence_generator(index, sub_sequence):  # Recursive Driver
        # Base Case
        if index == n:
            sub_sequences.append(sub_sequence)
            return
        # Recursive Case
        else:
            if type(iterable) == list:
                included_sub_sequence = sub_sequence.copy()
                included_sub_sequence.append(iterable[index])
                recursive_sub_sequence_generator(index + 1, sub_sequence)  # Exclude element
                recursive_sub_sequence_generator(index + 1, included_sub_sequence)  # Include element
            else:
                included_sub_sequence = sub_sequence + iterable[index]
                recursive_sub_sequence_generator(index + 1, sub_sequence)  # Exclude char
                recursive_sub_sequence_generator(index + 1, included_sub_sequence)  # Include Char

    iterable_type = type(iterable)
    if iterable_type == list:
        recursive_sub_sequence_generator(0, [])
    else:
        recursive_sub_sequence_generator(0, "")
    return sub_sequences


def generate_all_sub_arrays_of_an_iterable(iterable) -> list:
    """
    Generates all contiguous sub arrays of an iterable
    Time Complexity: O(n^3)
    Space Complexity: O(2^N)
    """
    n: int = len(iterable)
    sub_arrays: list = []
    for i in range(n):
        for j in range(i, n):
            sub_array: list = iterable[i: j + 1]
            if type(iterable) == list:
                sub_arrays.append(sub_array.copy())
            else:
                sub_arrays.append(sub_array)
    return sub_arrays
