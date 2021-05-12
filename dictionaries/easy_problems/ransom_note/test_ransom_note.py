import unittest

from .brute_force import check_magazine


class TestRansomNote(unittest.TestCase):
    functionality_test_data: dict = {
        "test_0": {
            "params": {
                "magazine": ["give", "me", "one", "grand", "today", "night"],
                "note": ["give", "one", "grand", "today"]
            },
            "expected": "Yes"
        },
        "test_1": {
            "params": {
                "magazine": ["two", "times", "three", "is", "not", "four"],
                "note": ["two" "times" "two" "is" "four"]
            },
            "expected": "No"
        },
        "test_2": {
            "params": {
                "magazine": ["ive" "got" "a" "lovely" "bunch" "of" "coconuts"],
                "note": ["ive", "got", "some", "coconuts"]
            },
            "expected": "No"
        },
    }

    def test0(self):
        magazine = ["give", "me", "one", "grand", "today", "night"]
        note = ["give", "one", "grand", "today"]
        ans = "Yes"
        result = check_magazine(magazine, note)
        self.assertEqual(ans, result)

    def test1(self):
        magazine = ["two", "times", "three", "is", "not", "four"]
        note = ["two" "times" "two" "is" "four"]
        ans = "No"
        result = check_magazine(magazine, note)
        self.assertEqual(ans, result)

    def test2(self):
        magazine = ["ive" "got" "a" "lovely" "bunch" "of" "coconuts"]
        note = ["ive", "got", "some", "coconuts"]
        ans = "No"
        result = check_magazine(magazine, note)
        self.assertEqual(ans, result)


if __name__ == "__main__":
    unittest.main()
