import unittest

from tools.iterables.sub_iterables import number_of_sub_arrays_in_an_iterable


class SubIterablesTester(unittest.TestCase):

    # Number of Sub Arrays in a String Tests ----------
    def test_that_number_of_sub_arrays_function_can_calculate_with_length_0(self):
        mock_length: int = 0
        expected: int = 0
        actual: int = number_of_sub_arrays_in_an_iterable(mock_length)
        self.assertEqual(expected, actual)

    def test_that_number_of_sub_arrays_function_can_calculate_with_length_1(self):
        mock_length: int = 1
        expected: int = 1
        actual: int = number_of_sub_arrays_in_an_iterable(mock_length)
        self.assertEqual(expected, actual)

    def test_that_number_of_sub_arrays_function_can_calculate_with_length_7(self):
        mock_length: int = 7
        expected: int = 28
        actual: int = number_of_sub_arrays_in_an_iterable(mock_length)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
