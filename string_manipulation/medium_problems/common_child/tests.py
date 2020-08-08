from unittest import TestCase, main
import time
import os

from .longest_common_subsequence_algs import *

currentPath = os.path.dirname(__file__)
testResourcesPath = currentPath + "/test_resources/"


class TestLcsAlgorithms(TestCase):

    functionalityTests = {
        "test0": ("ABCD", "ABDC", 3),
        "test1": ("AA", "BB", 0),
        "test2": ("HARRY", "SALLY", 2),
        "test3": ("SHINCHAN", "NOHARAAA", 3),
        "test4": ("ABCDEF", "FBDAMN", 2)
        }

    timeComplexityTests = {
        "tc_test0": ("time_complexity_test_0.txt", 1417)
        }

    def testCommonChildTimeComplexity(self):
        print("\nCommon Child Time Complexity Tests")
        for testName, testData in self.timeComplexityTests.items():
            s1: str = ""
            s2: str = ""
            with open(testResourcesPath + testData[0], "r") as reader:
                lines = reader.readlines()
                s1 = lines[0]
                s2 = lines[1]
            ans = testData[1]

            tic = time.perf_counter()
            result = commonChild(s1, s2)
            tock = time.perf_counter()
            timeLog = f"\nCommonChild finished in {tock - tic:0.4f} seconds given two {len(s1)} length strings"
            print(timeLog)

            self.assertEqual(ans, result)

    def testCommonChild(self):
        print("\nCommon Child Tests")
        for testName, testData in self.functionalityTests.items():
            s1 = testData[0]
            s2 = testData[1]
            ans = testData[2]
            result = commonChild(s1, s2)
            print(f"\n{testName}") 
            self.assertEqual(ans, result)
        print("\n")

    def testMemoizedIterativeApproach(self):
        print("\nMemoized Iterative Approach Tests")
        for testName, testData in self.functionalityTests.items():
            s1 = testData[0]
            s2 = testData[1]
            ans = testData[2]
            result = getLCSMemoizedIterativeApproach(s1, s2)
            print(f"\n{testName}")
            self.assertEqual(ans, result)
        print("\n")

    def testMemoizedApproach(self):
        print("\nMemoized Approach Tests")
        for testName, testData in self.functionalityTests.items():
            s1 = testData[0]
            s2 = testData[1]
            ans = testData[2]
            result = getLCSMemoizedApproach(s1, s2)
            print(f"\n{testName}")
            self.assertEqual(ans, result)
        print("\n")

    def testBottomUp(self):
        print("\nBottom Up Tests")
        for testName, testData in self.functionalityTests.items():
            s1 = testData[0]
            s2 = testData[1]
            ans = testData[2]
            result = getLCSBottomUp(s1, s2)
            print(f"\n{testName}")
            self.assertEqual(ans, result)
        print("\n")

    def testBackwardApproach(self):
        print("\nBackward Approach Tests")
        for testName, testData in self.functionalityTests.items():
            s1 = testData[0]
            s2 = testData[1]
            ans = testData[2]
            result = getLCSBackwardApproach(s1, s2)
            print(f"\n{testName}")
            self.assertEqual(ans, result)
        print("\n")

    def testBruteForce(self):
        print("\nBrute Force Tests")
        for testName, testData in self.functionalityTests.items():
            s1 = testData[0]
            s2 = testData[1]
            ans = testData[2]
            result = getLCSBruteForce(s1, s2)
            print(f"\n{testName}")
            self.assertEqual(ans, result)
        print("\n")


if __name__ == "__main__":
    main()
