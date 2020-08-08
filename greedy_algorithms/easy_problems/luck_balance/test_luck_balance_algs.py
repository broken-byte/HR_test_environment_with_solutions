from unittest import TestCase, main
import os
import time

from .luck_balance_algs import getMaxLuckBalanceBruteForceApproach
from test_utilities.test_variables import console_break_line

currentPath = os.path.dirname(__file__)
testResourcesPath = currentPath + "/test_resources/"


class TestLuckBalanceAlgs(TestCase):

    functionalityTests: dict = {
        "test_0": {
            "k": 2,
            "contests": [
                [5, 1],
                [1, 1],
                [4, 0],
                ],
            "expected": 10
        },
        "test_1": {
            "k": 1,
            "contests": [
                [5, 1],
                [1, 1],
                [4, 0],
                ],
            "expected": 8
        },
        "test_2": {
            "k": 3,
            "contests": [
                [5, 1],
                [2, 1],
                [1, 1],
                [8, 1],
                [10, 0],
                [5, 0]
                ],
            "expected": 29
        },
        "test_3": {
            "k": 5,
            "contests": [
                [13, 1],
                [10, 1],
                [9, 1],
                [8, 1],
                [13, 1],
                [12, 1],
                [18, 1],
                [13, 1]
                ],
            "expected": 42
        },
        "test_4": {
            "k": 2,
            "contests": [
                [5, 1],
                [4, 0],
                [6, 1],
                [2, 1],
                [8, 0]
                ],
            "expected": 21
        }
    }

    timeComplexityTests = {
        "tc_test0": ("time_complexity_test_0.txt", 494906)
        }

    def testBruteForceApproach(self):
        print("Brute Force Functionality Tests\n", console_break_line)
        for testName, testData in self.functionalityTests.items():
            try:
                expected: int = testData["expected"]
                k: int = testData["k"]
                contests: list = testData["contests"]
                actual: int = getMaxLuckBalanceBruteForceApproach(k, contests)
                print(testName, testData, actual)
                self.assertEqual(expected, actual)

            except AssertionError as error:
                print(error)

    def testBruteForceTimeComplexity(self):
        print("\nBrute Force Time Complexity Tests\n", console_break_line)
        for testName, testData in self.timeComplexityTests.items():
            k: int = 0
            contests: list = []
            k, contests = self.processTimeComplexityTestFile(testData[0])
            expected: int = testData[1]
            actual = self.getConsoleTimeLoggedResult(k, contests)
            print(testName, k, contests, expected)
            self.assertEqual(expected, actual)

    def getConsoleTimeLoggedResult(self, k: int, contests: list) -> int:
        tic = time.perf_counter()
        actual = getMaxLuckBalanceBruteForceApproach(k, contests)
        tock = time.perf_counter()
        timeLog = f"\nBrute Force Approach finished in {tock - tic:0.10f} seconds given {len(contests)} sized contest array\n"
        print(timeLog)
        return actual

    def processTimeComplexityTestFile(self, testFileName: str) -> tuple:
        k: int = 0
        contests: list = []

        with open(testResourcesPath + testFileName, "r") as f:
            for index, line in enumerate(f):
                processedLine = self.processLine(line)
                if index == 0:
                    k = processedLine[1]
                else:
                    luckBalance, contestImportance = processedLine
                    contests.append([luckBalance, contestImportance])

        return k, contests

    def processLine(self, contestLine: str) -> list:
        contestLine = contestLine.strip("\n")
        contestLine = contestLine.split(" ")
        contestLine = [int(element) for element in contestLine]
        return contestLine


if __name__ == "__main__":
    main()
