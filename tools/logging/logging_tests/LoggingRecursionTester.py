import unittest

from tools.logging.recursion import log_recursion


class LoggingRecursionTester(unittest.TestCase):
    def test_that_recursion_logger_logs_correct_message(self):
        mock_recursion_level: int = 3
        mock_parameters: dict = {
            "array_1": [1, 2, 3],
            "array_2": [4, 5, 6]
        }
        expected: str = (f"=============== Recursion Logger ===============\n"
                         f"Recursion level: {mock_recursion_level}\n"
                         f"array_1: [1, 2, 3]\n"
                         f"array_2: [4, 5, 6]\n")
        actual: str = log_recursion(mock_recursion_level, testable=True, **mock_parameters)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
