import unittest
import os
import random
import string
import time

from .specialStringAgain import substrCount, substrCountSlow

currentPath = os.path.dirname(__file__)
testResourcesPath = currentPath + "/testResources/"


def generateRandomString(sizeOfString: int) -> str:
    randomString = ''.join(random.choices(string.ascii_lowercase, k = sizeOfString))   
    return randomString


class TestSubstrCount(unittest.TestCase):
    
    def test1(self):
        n = 5
        s = "asasd"
        ans = 7
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def test2(self):
        n = 7
        s = "abcbaba"
        ans = 10
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def test3(self):
        n = 4
        s = "aaaa"
        ans = 10
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def test4(self):
        n = 8
        s = "mnonopoo"
        ans = 12
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def testTimeComplexity(self):
        n = 327308
        s = ""
        with open(testResourcesPath + "testCase5.txt", "r") as reader:
            for line in reader.readlines():
                s += line
        ans = 393074

        tic = time.perf_counter()
        result = substrCount(n, s)
        tock = time.perf_counter()
        print(f"\nsubstrCount() finished in {tock - tic:0.4f} seconds given a 327,308 character string")


        self.assertEquals(ans, result) 

    def test5(self): 
        n = 11
        s = "aaaabbbaaaa"
        ans = 26
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def test6(self): 
        n = 22
        s = "ftglowerfthilowskqaaaa"
        ans = 28
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def test7Random(self):
        n = 20
        s = generateRandomString(n)
        ans = substrCountSlow(n, s)
        result = substrCount(n, s)

        self.assertEquals(ans, result)
        #print(f"Test8String: {s}")

    def test8Random(self):
        n = 15
        s = generateRandomString(n)
        ans = substrCountSlow(n, s)
        result = substrCount(n, s)

        self.assertEquals(ans, result)

    def testFindError(self):
        s = ""
        ans = None
        foundError = False
        count = 0
        while not foundError:
            s = generateRandomString(15)
            ans = substrCountSlow(15, s)
            result = substrCount(15, s)
            if ans != result: 
                foundError = True
                print(f"ErrorString: {s}, answer: {ans}")
            if count > 100: break
            count += 1

    def test9(self):
        s = "qbvpqggkggfmnsp"
        n = 15
        ans = 19
        result = substrCount(n, s)

        self.assertEqual(ans, result)

    def test10(self):
        s = "dtgbwzzfzuhtmcz"
        n = 15
        ans = 17
        result = substrCount(n, s)

        self.assertEqual(ans, result)

    def test11(self):
        s = "qgntozqcotcoiat"
        n = 15
        ans = 15
        result = substrCount(n, s)
        self.assertEqual(ans, result)
        
        
if __name__ == "__main__":
    unittest.main()