
def commonChild(s1: str, s2: str) -> int:
    '''
    The implementation that will ultimately be submitted to 
    HackerRank for evaluation, using the most optimal algorithm
    in this file!
    Current implementation: getMemoizedIterativeApproach()
    '''
    n = len(s1)
    m = len(s2)
    memo = [[0]* (n + 1) for _ in range(m + 2)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
            else:
                comparison1 = memo[i + 1][j]
                comparison2 = memo[i][j + 1]
                memo[i + 1][j + 1] = max(comparison1, comparison2)
    return memo[n][m]

def getLCSMemoizedIterativeApproach(s1: str, s2: str) -> int: # O(n*m)
    '''
    Dynamic Programming approach utilizing a 2D memo array but using iteration
    vs. recursion to solve a stack limit issue with VSCode. 
        - Time Complexity: O(n*m)
    '''
    n = len(s1)
    m = len(s2)
    memo = [[0]* (n + 1) for _ in range(m + 2)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
            else:
                comparison1 = memo[i + 1][j]
                comparison2 = memo[i][j + 1]
                memo[i + 1][j + 1] = max(comparison1, comparison2)
    return memo[n][m]

def getLCSMemoizedApproach(s1: str, s2: str) -> int: # Total Time Complexity = O(n*m)
    '''
    Recursive bottom up approach that utilizes a 2D memo array, optimizes from O(2^n) -> O(n*m).
    - Time Complexity: O(N*m)
    '''
    n = len(s1)
    m = len(s2)
    memo = [[None for _ in range(m)] for _ in range(n)]

    def longestCommonSubsequenceGenerator(i: int , j: int) -> int: # O(n*m)
        '''Recursive driver function for LCS'''
        if i == len(s1) or j == len(s2): # Base Case
            return 0
        elif memo[i][j] != None: # Memoized Case
            return memo[i][j]
        elif s1[i] == s2[j]:
            result = 1 + longestCommonSubsequenceGenerator(i + 1, j + 1)
        elif s1[i] != s2[j]:
            comparison1 = longestCommonSubsequenceGenerator(i + 1, j)
            comparison2 = longestCommonSubsequenceGenerator(i, j + 1)
            result = max(comparison1, comparison2)
        memo[i][j] = result
        return result

    lcsLength = longestCommonSubsequenceGenerator(0, 0)
    return lcsLength

def getLCSBottomUp(s1: str, s2: str) -> int:
    '''
    Bottom up recursive approach that starts from indices 0, 0
    - Time Complexity: O(2^n)
    '''
    n, m = len(s1), len(s2)

    def longestCommonSubSequenceGenerator(s1: str, s2: str, i: int, j: int) -> int:
        '''Recursive driver function for LCS'''
        if i == n or j == m: # Base Case
            result = 0
        elif s1[i] == s2[j]:
            result = 1 + longestCommonSubSequenceGenerator(s1, s2, i + 1, j + 1)
        elif s1[i] != s2[j]:
            comparison1 = longestCommonSubSequenceGenerator(s1, s2, i + 1, j)
            comparison2 = longestCommonSubSequenceGenerator(s1, s2, i, j + 1)
            result = max(comparison1, comparison2)
        return result

    lcsLength = longestCommonSubSequenceGenerator(s1, s2, 0, 0)
    return lcsLength

def getLCSBackwardApproach(s1: str, s2: str)-> int:
    '''
    Backward recursive approach that starts at the ends of the strings
    - Time Complexity: O(2^n)
    '''
    n, m = len(s1), len(s2)

    def longestCommonSubsequenceGenerator(s1: str, s2: str, n: int, m: int) -> int: # O(2^(n + m)
        '''Recursive driver function for LCS'''
        if n == 0 or m == 0: # Base Case
            result = 0
        elif s1[n - 1] == s2[m - 1]: # Matching Recursive Case
            result = 1 + longestCommonSubsequenceGenerator(s1, s2, n - 1, m - 1)
        elif s1[n - 1] != s2[m - 1]: # Different Recursive Case
            temp1 = longestCommonSubsequenceGenerator(s1, s2, n - 1, m)
            temp2 = longestCommonSubsequenceGenerator(s1, s2, n, m - 1)
            result = max(temp1, temp2)
        return result

    lcsLength = longestCommonSubsequenceGenerator(s1, s2, n, m)
    return lcsLength

def getLCSBruteForce(s1: str, s2: str) -> int: # Total Time Complexity = O(2^n)
    '''
    Trivial brute force approach that gets all subsequences possible and compares.
    - Time Complexity: O(2^n)
    '''
    subSequences1 = set(generateAllSubSequencesOfAString(s1)) # O(2^n)
    subSequences2 = set(generateAllSubSequencesOfAString(s2)) # O(2^n)

    commonSequencesBetween1And2 = subSequences1.intersection(subSequences2) # O(2*2^n

    lengthsOfCommonSequencesBetween1And2 = [len(sub) for sub in commonSequencesBetween1And2] # O(2*2^n)
    longestCommonSubsequenceLength = max(lengthsOfCommonSequencesBetween1And2) # # O(2*2^n)
    return longestCommonSubsequenceLength

def generateAllSubSequencesOfAString(s: str) -> list: # Total Time Complexity = O(2^n)
    '''
    Helper function to recursively generate all subsequences of string: s.
    - Time Complexity: O(2^n)
    '''
    n = len(s)
    subSequences = []

    def recursiveSubSequenceGenerator(index, subString):
        '''Recursion driver'''
        # Base Case
        if index == n:
            subSequences.append(subString)
            return
        # Recursive Case
        else:
            recursiveSubSequenceGenerator(index + 1, subString) # Exclude char
            recursiveSubSequenceGenerator(index + 1, subString + s[index]) # Include Char      

    recursiveSubSequenceGenerator(0, "")
    return subSequences
    
if __name__ == "__main__":
    pass

