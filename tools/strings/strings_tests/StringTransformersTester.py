import unittest

from tools.strings.string_transformers import capitalize_character_at, delete_character_at


class MyTestCase(unittest.TestCase):

    # Capitalization Function Tests ----------------------------------
    def test_that_capitalizer_can_capitalize_first_letter(self):
        mock_string: str = "hello"
        mock_index: int = 0
        expected: str = "Hello"
        actual: str = capitalize_character_at(mock_index, mock_string)
        self.assertEqual(expected, actual)

    def test_that_capitalizer_can_capitalize_second_letter(self):
        mock_string: str = "hello"
        mock_index: int = 1
        expected: str = "hEllo"
        actual: str = capitalize_character_at(mock_index, mock_string)
        self.assertEqual(expected, actual)

    def test_that_capitalizer_can_capitalize_last_letter(self):
        mock_string: str = "hello"
        mock_index: int = len(mock_string) - 1
        expected: str = "hellO"
        actual: str = capitalize_character_at(mock_index, mock_string)
        self.assertEqual(expected, actual)

    # Deletion Function Tests ----------------------------------------
    def test_that_deletor_can_delete_first_letter(self):
        mock_string: str = "hello"
        mock_index: int = 0
        expected: str = "ello"
        actual: str = delete_character_at(mock_index, mock_string)
        self.assertEqual(expected, actual)

    def test_that_deletor_can_delete_second_letter(self):
        mock_string: str = "hello"
        mock_index: int = 1
        expected: str = "hllo"
        actual: str = delete_character_at(mock_index, mock_string)
        self.assertEqual(expected, actual)

    def test_that_deletor_can_delete_last_letter(self):
        mock_string: str = "hello"
        mock_index: int = len(mock_string) - 1
        expected: str = "hell"
        actual: str = delete_character_at(mock_index, mock_string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
