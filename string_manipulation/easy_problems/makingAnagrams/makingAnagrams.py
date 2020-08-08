
def makingAnagrams(a: str, b: str) -> int:
    '''
    Given two strings a, b, returns the minimum number
    of deletions from either string needed to make a and b 
    anagrams of each other. 
    '''
    countOfDeletionsNeeded = 0
    uniqueCharactersInBoth = set(a + b)
    counterA = customCounter(uniqueCharactersInBoth, a)
    counterB = customCounter(uniqueCharactersInBoth, b)
    for character in uniqueCharactersInBoth:
        countOfDeletionsNeeded += abs(counterA[character] - counterB[character])
    return countOfDeletionsNeeded
    
def customCounter(uniqueCharacters: set, string: str) -> dict:
    '''
    Given a set of all the unique instances of  different characters
    in a string and said string, returns an instance counter dictionary 
    '''
    counter = {}
    for character in uniqueCharacters:
        if character in string:
            count = 0
            for char in string:
                if character == char:
                    count += 1
            counter[character] = count
        else:
            counter[character] = 0
    return counter

def main():
    pass

if __name__ == "__main__":
    main()