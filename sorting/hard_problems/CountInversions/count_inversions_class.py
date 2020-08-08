

class CountInversions:
    '''
    The solution to this problem in class form along
    with an implementation of the regular mergesort
    function that I used to guide my intuition of the 
    inversion count function
    '''

    inversionCount = 0

    def __init__(self):
        pass

    def getInversionCount(self, array: list) -> int:
        '''
        Given an array of numbers, returns the number 
        of inversions within the array.
            - Time Complexity: O(N*log(N))
        '''
        print(f"Starting array: {array}")
        sortedArray, inversionCount = self.sortAndCount(array)
        print(f"sorted array: {sortedArray}")
        return inversionCount

    def mergeSort(self, array: list) -> list:
        
        # Base Case
        if len(array) <= 1: return array

        # Recursive Case
        middle = int(len(array)/2)

        left = self.mergeSort(array[:middle])
        
        right = self.mergeSort(array[middle:])
    

        return self.merge(left, right)

    def merge(self, leftArray: list, rightArray: list) -> list:
            
        print(f"\nMerging left array: {leftArray} with right array: {rightArray}\n")

        mergedArray = [] # Final ouput array
        leftLength = len(leftArray)
        rightLength = len(rightArray)
        leftCursor = 0
        rightCursor = 0

        while leftCursor < leftLength and rightCursor < rightLength:

            if leftArray[leftCursor] < rightArray[rightCursor]:
                mergedArray.append(leftArray[leftCursor])
                leftCursor += 1
                

            else:
                mergedArray.append(rightArray[rightCursor])
                rightCursor += 1
            
            print(f"Merged Array so far: {mergedArray}\n")
                

        if leftCursor == leftLength:
            mergedArray.extend(rightArray[rightCursor:])

        else:
            mergedArray.extend(leftArray[leftCursor:])

        print(f"merged: {mergedArray}")
        return mergedArray

    def sortAndCount(self, array: list) -> tuple:
        '''
        Given an array of numbers, returns the sorted
        array as well as the number of inversions within 
        the array.
            - Time Complexity: O(N*log(N))
        '''
        inversionCount = 0

        # Base Case
        if len(array) <= 1: return array, inversionCount

        # Recursive Case
        middle = int(len(array)/2)

        leftArray, leftInversionCount = self.sortAndCount(array[:middle])
        rightArray, rightInversionCount = self.sortAndCount(array[middle:])

        mergedArray, mergedInversionCount = self.mergeAndCount(leftArray, rightArray)

        print(f"Left: {leftArray}, Right: {rightArray}, merged: {mergedArray}")
        print(f"left inversions: {leftInversionCount}, right inversions: {rightInversionCount}, merged Inversions: {mergedInversionCount}")
        
        totalInversionCount = leftInversionCount + rightInversionCount + mergedInversionCount

        print(f"Total inversions: {totalInversionCount}")

        return mergedArray, totalInversionCount

    def mergeAndCount(self, leftArray: list, rightArray: list) -> tuple:
        '''
        Given two sorted arrays, knits them together in sorted 
        order and returns as one unified list along with the inversion count
        '''
        print(f"\nMerging left array: {leftArray} with right array: {rightArray}\n")

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
                mergedInversionCount += len(leftArray[leftCursor:])
                rightCursor += 1

            print(f"Merged Array so far: {mergedArray}\n")
                
                
        if leftCursor == leftLength:
            mergedArray.extend(rightArray[rightCursor:])

        else:
            mergedArray.extend(leftArray[leftCursor:])

        print(f"merged: {mergedArray}")

        print(f"Number of inversions in this merge: {mergedInversionCount}")

        return mergedArray, mergedInversionCount
        