
def alternatingCharacters(s: str) -> int:
    '''
    Given a string with only characters "A", and "B", 
    returns the minimum number of deletions needed such that
    there are no matching adjacent characters.
    '''
    minDeletions = 0
    for index in range(len(s) - 1):
        if s[index] == s[index + 1]: minDeletions += 1
    return minDeletions

def main():
    pass

if __name__ == "__main__": 
    main()