import unittest

from .frequency_queries import frequencyQueries


class TestFrequencyQueries(unittest.TestCase):

    def test0(self):
        queries = [
            (1,1), 
            (2,2), 
            (3,2), 
            (1,1), 
            (1,1), 
            (2,1), 
            (3,2)
            ]
        ans = [0, 1]
        result = frequencyQueries(queries)
        self.assertEqual(ans, result)

    def test1(self):
        queries = [
            (1, 5),
            (1, 6),
            (3, 2),
            (1, 10),
            (1, 10),
            (1, 6),
            (2, 5),
            (3, 2)
            ]
        ans = [0, 1]
        result = frequencyQueries(queries)
        self.assertEqual(ans, result)

    def test2(self):
        queries = [
            (3, 4),
            (2, 1003),
            (1, 16),
            (3, 1)
            ]
        ans = [0, 1]
        result = frequencyQueries(queries)
        self.assertEqual(ans, result)

    def test3(self):
        queries = [
            (1, 3),
            (2, 3),
            (3, 2),
            (1, 4),
            (1, 5),
            (1, 5),
            (1, 4),
            (3, 2),
            (2, 4),
            (3, 2)
        ]
        ans = [0, 1, 1]
        result = frequencyQueries(queries)
        self.assertEqual(ans, result)

if __name__ == "__main__":
    unittest.main()