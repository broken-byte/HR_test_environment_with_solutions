from unittest import TestCase, main

from .new_years_chaos_algs import minimumBribes


class TestNewYearsChaosAlgs(TestCase):

    def test_validQueueShouldReturnMinimumBribe0(self):
        queue: list = [2, 1, 5, 3, 4]
        expected: int = 3
        actual: int = minimumBribes(queue)
        self.assertEqual(expected, actual)

    def test_validQueueShouldReturnMinimumBribe1(self):
        queue: list = [1, 2, 5, 3, 7, 8, 6, 4]
        expected: int = 7
        actual: int = minimumBribes(queue)
        self.assertEqual(expected, actual)

    def test_chaoticQueueShouldReturnNegativeOne0(self):
        queue: list = [2, 5, 1, 3, 4]
        expected: int = -1
        actual: int = minimumBribes(queue)
        self.assertEqual(expected, actual)

    def test_chaoticQueueShouldReturnNegativeOne1(self):
        queue: list = [5, 1, 2, 3, 7, 8, 6, 4]
        expected: int = -1
        actual: int = minimumBribes(queue)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    main()