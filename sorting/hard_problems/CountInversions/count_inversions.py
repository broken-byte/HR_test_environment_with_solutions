from random import randint

'''
Given an array of numbers, return the number 
of inversions within the array in O(n*log(n))
time complexity. 

an inversion is when some indices i and j
are i < j, and for some array arr[], a[i] > a[j]

Solution: Use a modified mergeSort()!
'''


def countInversions(arr: list) -> int:
    '''
    Given an array of numbers, returns the number 
    of inversions within the array.
        - Time Complexity: O(N*log(N))
    '''
    inversionCount = sortAndCount(arr)

    return inversionCount[1]

def sortAndCount(array: list) -> tuple:
    '''
    Recursive modified mergesort that counts
    inversions while sorting
    '''
    inversionCount = 0
    arrayLength = len(array)

    # Base Case
    if arrayLength <= 1: return array, inversionCount

    # Recursive Case
    middle = int(arrayLength/2)

    leftArray, leftInversionCount = sortAndCount(array[:middle])
    rightArray, rightInversionCount = sortAndCount(array[middle:])

    mergedArray, mergedInversionCount = mergeAndCount(leftArray, rightArray) 
    totalInversionCount = leftInversionCount + rightInversionCount + mergedInversionCount

    return mergedArray, totalInversionCount

def mergeAndCount(leftArray: list, rightArray: list) -> tuple:
    '''
    Given two sorted arrays, knits them together in sorted 
    order and returns as one unified list along with the inversion count
    '''
    mergedArray = [] # Final ouput array
    leftLength = len(leftArray)
    rightLength = len(rightArray)
    leftCursor = 0
    rightCursor = 0
    mergedInversionCount = 0

    while leftCursor < leftLength and rightCursor < rightLength:

        if leftArray[leftCursor] <= rightArray[rightCursor]:
            mergedArray.append(leftArray[leftCursor])
            leftCursor += 1
        
        else:
            mergedArray.append(rightArray[rightCursor])
            mergedInversionCount += leftLength - leftCursor
            rightCursor += 1           
            
    if leftCursor == leftLength:
        mergedArray.extend(rightArray[rightCursor:])

    else:
        mergedArray.extend(leftArray[leftCursor:])

    return mergedArray, mergedInversionCount

def createArray(size = 10, maxValue = 50) -> list:
    return [randint(0, maxValue) for _ in range(size)]

def main():

    testArray1 = [1,1,1,2,2]
    testArray2 = [2,1,3,1,2]

    testArray1Answer = 0
    testArray2Answer = 4

    result1 = countInversions(testArray1)
    result2 = countInversions(testArray2)

    print("\n")
    print(result1)
    print(testArray1Answer)
    print(result2)
    print(testArray2Answer)
   
if __name__ == "__main__":
    main()

