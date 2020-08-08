  
def getAllAnagramPairsIn(s):
    n = len(s)
    numberOfAnagramPairs = 0

    for i in range(1, n): # length of the sublist 
        subStringsWithCounts = {}

        for j in range(n - i + 1): # Number of sublists in this iteration
            subString = s[j: j + i]
            sortedSubList = sorted(list(subString))

            sortedSubString = "".join(sortedSubList) # Convert the sortedSubList back into a string

            if sortedSubString not in subStringsWithCounts: # There hasn't been a match of the sortedSubString
                subStringsWithCounts[sortedSubString] = 1

            else: # There is a match, add to the number of instances of that sortedSubString
                subStringsWithCounts[sortedSubString] += 1

            numberOfAnagramPairs += subStringsWithCounts[sortedSubString] - 1
            '''
            Now, the above line of code might be confusing.

            - Why increment AFTER the above conditional?

            - Why increment by subStringsWithCounts[subString]?

            - Why substract by 1?

            After the conditional, subStringsWithCounts[substring] will
            always have AT LEAST 1, or in other words there is
            an instance of this substring present in the dictionary.
            We need this value in order to calculate the below information:

            To explain the calculation of subStringsWithCounts[subString] - 1, 
            We must first walk through a small thought experiment:

                How many pairs can one make given n items?
                
                Let's start with 1 item in our "Bag" ():
                (item1) => 0 pairs since theirs only one item
                (item1, item2) => 0 + 1 pair = 1 pair!
                (item1, item2, item3) =>  1 + 2 pairs = 3 pairs!
                etc....

                The pattern of number of pairs for n items can be
                reflected in the following equation: 
                numberOfPairs = previousAmountOfPairs + (numberOfItems - 1)

            Voila! We have our calculation. This is why we increment 
            numberOfAnagramPairs by subStringsWithCounts[subString] - 1!
            That is the direct reflection of: 
            numberOfPairs = previousAmountOfPairs + (numberOfItems - 1)
            In our code!
            '''
    return numberOfAnagramPairs
            
def main():

    tests = ["mom", "abba", "abcd", "ifailuhkqq", "kkkk"]

    for test in tests:
        getAnagramCountsInString(test)
        print("=============================================================================================\n")

if __name__ == "__main__":
    main()