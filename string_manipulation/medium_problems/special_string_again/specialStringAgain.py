
def substrCount(n: int, s: str)-> int: # O(N)
    '''
    Single pass with branch out strategy
        Time Complexity: O(N)
    '''
    specialStringCount = n # Every individual character is a special string
    consecutiveCharacter = s[0] # Buffer for repeating char
    consecutiveCharacterCount = 1 # count of repeating chars
    for index in range(n - 1):
        if s[index + 1] == consecutiveCharacter: # Check for repeating chars
            consecutiveCharacterCount += 1
        else: 
            # Use math formula for # of subs in a string minus each individual 
            # character count (already counted that up top)
            nestedSpecialStringsSoFar = numberOfPossibleSubStringsInAString(consecutiveCharacterCount)
            specialStringCount +=  nestedSpecialStringsSoFar - consecutiveCharacterCount
            # Start branching out from first dissimilar character to check if 
            # Middle char special string
            numberOfSameCharactersOnLeft = consecutiveCharacterCount
            numberOfSameCharactersOnRight = 0
            middleCharacterIndex = index + 1
            branchOutStart = middleCharacterIndex + 1
            endOfRightSideIndex = middleCharacterIndex + numberOfSameCharactersOnLeft
            for branchoutIndex in range(branchOutStart, endOfRightSideIndex + 1): 
                if branchoutIndex < n and s[branchoutIndex] == consecutiveCharacter: 
                    numberOfSameCharactersOnRight += 1
                else: break
            # We've found a middle character special string!
            if (numberOfSameCharactersOnLeft >= numberOfSameCharactersOnRight and 
                numberOfSameCharactersOnRight > 0): 
                specialStringCount += numberOfSameCharactersOnRight
            # Reset consecutiveCharacter 
            consecutiveCharacter = s[index + 1]
            consecutiveCharacterCount = 1
    # Check to see if we've looped through a long chain of consecutive chars
    # Without end
    if consecutiveCharacterCount > 1: 
        nestedSpecialStringsSoFar = numberOfPossibleSubStringsInAString(consecutiveCharacterCount)
        specialStringCount += nestedSpecialStringsSoFar - consecutiveCharacterCount

    return specialStringCount

def substrCountSlow(n: int, s: str) -> int: # O(n^2)
    '''
    Works reliably and simple to understand
    but does not meet the runtime complexity 
    requirements of the hackerank test
        Time Complexity: O(N^2)
    '''
    if allCharsEqual(s): return numberOfPossibleSubStringsInAString(n) # Efficient for all equal case
    subStrings = getSubStringsGreaterThanLengthOne(n, s) # O(n^2)
    specialStringCount = n
    for sub in subStrings: #~= O(n)* O(n) = O(n^2)
        if isSpecial(sub):
            specialStringCount += 1
    return specialStringCount

def numberOfPossibleSubStringsInAString(sizeOfString: int) -> int:
    '''Math formula'''
    return int((sizeOfString**2 + sizeOfString) / 2)


def getSubStringsGreaterThanLengthOne(n: int, s: str) -> list:  # O(n^2)
    subStrings = []
    for i in range(n): 
        sub="" 
        for j in range(i,n): 
            sub += s[j]
            if len(sub) != 1: subStrings.append(sub)
    return subStrings

def isSpecial(subString: str) -> bool: # O(n) + O(n) <= O(n)
    if allCharsEqual(subString): 
        return True
    elif allCharsExceptMiddleEqual(subString): 
        return True
    else: 
        return False

def allCharsEqual(s: str) -> bool: # O(n)
    if s == len(s) * s[0]: 
        return True

def allCharsExceptMiddleEqual(s: str) -> bool: # O(n)
    n = len(s)
    if n % 2 == 0: return False # Even strings have no middle
    middle = int(n / 2)
    s = s[:middle] + s[middle + 1:]
    if allCharsEqual(s): return True
    
def main():
    pass

if __name__ == "__main__":
    main()