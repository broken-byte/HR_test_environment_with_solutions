import unittest

from tools.iterables.sub_iterables import \
    get_number_of_sub_arrays_in_an_iterable, \
    generate_all_sub_sequences_of_an_iterable


class SubIterablesTester(unittest.TestCase):

    # Number of Sub Arrays in a String Tests ----------
    def test_that_number_of_sub_arrays_function_can_calculate_with_length_0(self):
        mock_length: int = 0
        expected: int = 0
        actual: int = get_number_of_sub_arrays_in_an_iterable(mock_length)
        self.assertEqual(expected, actual)

    def test_that_number_of_sub_arrays_function_can_calculate_with_length_1(self):
        mock_length: int = 1
        expected: int = 1
        actual: int = get_number_of_sub_arrays_in_an_iterable(mock_length)
        self.assertEqual(expected, actual)

    def test_that_number_of_sub_arrays_function_can_calculate_with_length_7(self):
        mock_length: int = 7
        expected: int = 28
        actual: int = get_number_of_sub_arrays_in_an_iterable(mock_length)
        self.assertEqual(expected, actual)

    # Sub Sequence Tests ------------------------------
    def test_that_sub_sequence_generator_can_generate_sub_sequences_for_strings(self):
        mock_string: str = "hello"
        expected: list = [
            '',
            'o',
            'l',
            'lo',
            'l',
            'lo',
            'll',
            'llo',
            'e',
            'eo',
            'el',
            'elo',
            'el',
            'elo',
            'ell',
            'ello',
            'h',
            'ho',
            'hl',
            'hlo',
            'hl',
            'hlo',
            'hll',
            'hllo',
            'he',
            'heo',
            'hel',
            'helo',
            'hel',
            'helo',
            'hell',
            'hello'
        ]
        actual: list = generate_all_sub_sequences_of_an_iterable("hello")
        self.assertEqual(expected, actual)

    def test_that_sub_sequence_generator_can_generate_sub_sequences_for_lists(self):
        mock_list: list = [1, 2, 3]
        expected: list = [
            [],
            [3],
            [2],
            [2, 3],
            [1],
            [1, 3],
            [1, 2],
            [1, 2, 3]
        ]
        actual: list = generate_all_sub_sequences_of_an_iterable(mock_list)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
