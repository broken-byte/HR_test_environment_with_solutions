import unittest

from .alternatingCharacters import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):

    def testNoDeletionsNeeded1(self):
        s = "ABABABAB"
        answer = 0
        result = alternatingCharacters(s)

        self.assertEquals(answer, result)

    def testNoDeletionsNeeded2(self):
        s = "BABABA"
        answer = 0
        result = alternatingCharacters(s)

        self.assertEquals(answer, result)

    def testSomeDeletionsNeeded1(self):
        s = "AAAA"
        answer = 3
        result = alternatingCharacters(s)

        self.assertEquals(answer, result)

    def testSomeDeletionsNeeded2(self):
        s = "BBBBB"
        answer = 4
        result = alternatingCharacters(s)

        self.assertEquals(answer, result)

    def testSomeDeletionsNeeded3(self):
        s = "AAABBB"
        answer = 4
        result = alternatingCharacters(s)

        self.assertEquals(answer, result)

    def testSomeDeletionsNeeded4(self):
        s = "AAABBBAABB"
        answer = 6
        result = alternatingCharacters(s)

        self.assertEquals(answer, result)

if __name__ == "__main__":
    unittest.main()

    