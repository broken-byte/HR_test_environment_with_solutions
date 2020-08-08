import unittest

from .ransom_note import checkMagazine


class TestRansomNote(unittest.TestCase):

    def test0(self):
        magazine = ["give", "me", "one", "grand", "today", "night"]
        note = ["give", "one", "grand", "today"]
        ans = "Yes"
        result = checkMagazine(magazine, note)
        self.assertEqual(ans, result)

    def test1(self):
        magazine = ["two", "times", "three", "is", "not", "four"]
        note = ["two" "times" "two" "is" "four"]
        ans = "No"
        result = checkMagazine(magazine, note)
        self.assertEqual(ans, result)

    def test2(self):
        magazine = ["ive" "got" "a" "lovely" "bunch" "of" "coconuts"]
        note = ["ive", "got", "some", "coconuts"]
        ans = "No"
        result = checkMagazine(magazine, note)
        self.assertEqual(ans, result)

if __name__ == "__main__":
    unittest.main()