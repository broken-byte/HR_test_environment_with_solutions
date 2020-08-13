import unittest

from .count_inversions import countInversions


class TestCountInversions(unittest.TestCase):

    def test0(self):
        arr = [1,1,1,2,2]
        answer = 0
        result = countInversions(arr)

        self.assertEquals(answer, result)

    def test1(self):
        arr = [2, 1, 3, 1, 2]
        answer = 4
        result = countInversions(arr)

        self.assertEquals(answer, result)

    def test2(self):
        arr = [2, 4, 1]
        answer = 2
        result = countInversions(arr)

        self.assertEquals(answer, result)


if __name__ == "__main__":
    unittest.main()
