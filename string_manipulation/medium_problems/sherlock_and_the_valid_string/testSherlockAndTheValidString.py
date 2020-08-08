import unittest

from .sherlockAndTheValidString import isValid


class TestSherlockAndTheValidString(unittest.TestCase):

    def testValidString1(self):
        s = "abc"
        answer = "YES"
        result = isValid(s)

        self.assertEqual(answer, result)

    def testValidString2(self):
        s = "abcdefghhgfedecba"
        answer = "YES"
        result = isValid(s)

        self.assertEqual(answer, result)


    def testInValidString1(self):
        s = "aabbcd"
        answer = "NO"
        result = isValid(s)

        self.assertEqual(answer, result)

    def testInValidString2(self):
        s = "aabbccddeefghi"
        answer = "NO"
        result = isValid(s)

        self.assertEqual(answer, result)

if __name__ == "__main__":
    unittest.main()

    
