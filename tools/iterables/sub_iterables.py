from tools.logging.recursion import log_recursion


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
    Recursively generate all subsequences of an iterable
    Time Complexity: O(2^n)
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
                recursive_sub_sequence_generator(index + 1, sub_sequence)  # Exclude char
                recursive_sub_sequence_generator(index + 1, included_sub_sequence)  # Include Char
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
