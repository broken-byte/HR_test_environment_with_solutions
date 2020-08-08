import unittest

from .makingAnagrams import makingAnagrams


class TestMakingAnagrams(unittest.TestCase):

    def testUnequalStrings1(self):
        a = "cde"
        b = "dcf"
        answer = 2
        result = makingAnagrams(a, b)

        self.assertEqual(answer, result)

    def testUnequalStrings2(self):
        a = "bacdc"
        b = "dcbad"
        answer = 2
        result = makingAnagrams(a, b)

        self.assertEqual(answer, result)

    def testEqualStrings1(self):
        a = "abcd"
        b = "abcd"
        answer = 0
        result = makingAnagrams(a, b)

        self.assertEqual(answer, result)

    def testEqualStrings2(self):
        a = "a"
        b = "a"
        answer = 0
        result = makingAnagrams(a, b)

        self.assertEqual(answer, result)

if __name__ == "__main__":
    unittest.main()
    