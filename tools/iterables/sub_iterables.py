

def number_of_sub_arrays_in_an_iterable(n: int) -> int:
    """
    Returns the number of sub arrays
    (consecutive, adjacent elements) in an iterable
    given the number of elements.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return int((n**2 + n) / 2)
