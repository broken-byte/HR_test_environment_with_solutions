import unittest

from dictionaries.medium_problems.sherlock_and_anagrams.sherlock_and_anagrams import getAllAnagramPairsIn


class TestSherlockAndAnagrams(unittest.TestCase):

    def test0(self):
        s = "mom"
        answer = 2
        result = getAllAnagramPairsIn(s)

        self.assertEquals(answer, result)

    def test1(self):
        s = "abba"
        answer = 4
        result = getAllAnagramPairsIn(s)

        self.assertEquals(answer, result)

    def test2(self):
        s = "abcd"
        answer = 0
        result = getAllAnagramPairsIn(s)

        self.assertEquals(answer, result)

    def test3(self):
        s = "ifailuhkqq"
        answer = 3
        result = getAllAnagramPairsIn(s)

        self.assertEquals(answer, result)

    def test4(self):
        s = "kkkk"
        answer = 10
        result = getAllAnagramPairsIn(s)

        self.assertEquals(answer, result)

    def test5(self):
        s = "cdcd"
        answer = 5
        result = getAllAnagramPairsIn(s)

        self.assertEquals(answer, result)

if __name__ == "__main__":
    unittest.main()
