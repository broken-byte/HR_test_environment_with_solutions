import unittest

from .count_triplets import countTriplets


class TestCountTriplets(unittest.TestCase):

    def test0(self):
        array = [1, 4, 16, 64]
        ans = 2
        ratio = 4
        result = countTriplets(array, ratio)
        self.assertEqual(ans, result)

    def test1(self):
        array = [1, 3, 9, 9, 27, 81]
        ans = 6
        ratio = 3
        result = countTriplets(array, ratio)
        self.assertEqual(ans, result)

    def test2(self):
        array = [1, 2, 2, 4]
        ans = 2
        ratio = 2
        result = countTriplets(array, ratio)
        self.assertEqual(ans, result)

    def test3(self):
        array = [1, 5, 5, 25, 125]
        ans = 4
        ratio = 5
        result = countTriplets(array, ratio)
        self.assertEqual(ans, result)

if __name__ == "__main__":
    unittest.main()
