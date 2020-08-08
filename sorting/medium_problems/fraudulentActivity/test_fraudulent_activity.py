from unittest import TestCase, main
import time
import os

from .fraudulentActivity import fraudulentNotifications

currentPath = os.path.dirname(__file__)
testResourcesPath = currentPath + "/test_resources/"


class TestFraudulentNotifications(TestCase):

    functionalityTests = {
        "test0": ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2),
        "test1": ([1, 2, 3, 4, 4], 4, 0),
        "test2": ([10, 20, 30, 40, 50], 3, 1),
        }

    timeComplexityTests = {
        "tc_test0": ("time_complexity_test_0.txt", 10000, 633)
        }

    def testBasicFunctionalityOfFraudulentNotifications(self):
        print("\nBasic Functionality Tests")
        for testName, testData in self.functionalityTests.items():
            expenditure = testData[0]
            d = testData[1] 
            ans = testData[2]
            result = fraudulentNotifications(expenditure, d)
            print(f"\n{testName}") 
            self.assertEqual(ans, result)
        print("\n")

    def testTimeComplexityOfFraudulentNotifications(self):
        print("\nTime Complexity Tests")
        for testName, testData in self.timeComplexityTests.items():
            expenditure = []
            with open(testResourcesPath + testData[0], "r") as reader:
                    line = reader.readline()
                    numberChars = line.split(' ')
                    for char in numberChars:
                        num = int(char)
                        expenditure.append(num)
            d = testData[1]
            ans = testData[2]
            tic = time.perf_counter()
            result = fraudulentNotifications(expenditure, d)
            tock = time.perf_counter()
            print(f"\nfraudulentNotifications() finished in {tock - tic:0.4f} seconds given a 200,000 length array of expenditures")
            self.assertEqual(ans, result)


if __name__ == "__main__":
    main()
