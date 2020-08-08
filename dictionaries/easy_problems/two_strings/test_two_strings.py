import unittest

from .two_strings import twoStrings


class TestTwoStrings(unittest.TestCase):

    def test0(self):
        s1 = "hello"
        s2 = "world"
        answer = "YES"
        result = twoStrings(s1, s2)

        self.assertEquals(answer, result)

    def test1(self):
        s1 = "hi"
        s2 = "world"
        answer = "NO"
        result = twoStrings(s1, s2)

        self.assertEquals(answer, result)


if __name__ == "__main__":
    unittest.main()