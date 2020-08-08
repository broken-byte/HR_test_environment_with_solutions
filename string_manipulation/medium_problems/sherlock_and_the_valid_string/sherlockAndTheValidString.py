import string 
import random

def isValid(s: str) -> str:
    '''
    Sherlock considers a string to be valid if all characters of the 
    string appear the same number of times. It is also valid if he can 
    remove just 1 character at 1 index in the string, and the remaining 
    characters will occur the same number of times. Given a string, 
    determine if it is valid. If so, return YES, otherwise return NO.
    '''
    frequencyOfDistinctCharactersInString = [s.count(letter) for letter in set(s) ]
    highestCount = max(frequencyOfDistinctCharactersInString)
    lowestCount = min(frequencyOfDistinctCharactersInString)
    if highestCount - lowestCount == 0: #If all values equal, return 'YES'
        return 'YES'
    #If difference between highest count and lowest count is 1
    #and there is only one letter with highest count, 
    #then return 'YES' (because we can subtract one of these 
    #letters and max=min , i.e. all counts are the same)
    elif (frequencyOfDistinctCharactersInString.count(highestCount) == 1 and 
          highestCount - lowestCount) == 1:
        return 'YES'

    #If the minimum count is 1
    #then remove this letter, and check whether all the other
    #counts are the same
    elif frequencyOfDistinctCharactersInString.count(lowestCount) == 1:
        frequencyOfDistinctCharactersInString.remove(lowestCount)
        # Recalculate 
        highestCount = max(frequencyOfDistinctCharactersInString)
        lowestCount = min(frequencyOfDistinctCharactersInString)
        # Check
        if highestCount - lowestCount == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

def generateRandomString() -> str:
    randomString = ''.join(random.choices(string.ascii_lowercase, k = 7))   
    return randomString

def main():
    pass
        
if __name__ == "__main__":
    main()