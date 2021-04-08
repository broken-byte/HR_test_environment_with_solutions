from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from dictionaries.medium_problems.sherlock_and_anagrams.test_resources.functionality_test_data import \
    functionality_test_data


def optimal(s: list) -> int:
    n = len(s)
    number_of_anagram_pairs = 0

    for i in range(1, n):  # length of the sublist
        sub_strings_with_counts = {}

        for j in range(n - i + 1):  # Number of sub lists in this iteration
            sub_string = s[j: j + i]
            sorted_sub_list = sorted(list(sub_string))

            sorted_sub_string = "".join(sorted_sub_list)  # Convert the sortedSubList back into a string

            if sorted_sub_string not in sub_strings_with_counts:  # There hasn't been a match of the sortedSubString
                sub_strings_with_counts[sorted_sub_string] = 1

            else:  # There is a match, add to the number of instances of that sortedSubString
                sub_strings_with_counts[sorted_sub_string] += 1

            number_of_anagram_pairs += sub_strings_with_counts[sorted_sub_string] - 1
            '''
            Now, the above line of code might be confusing.

            - Why increment AFTER the above conditional?

            - Why increment by subStringsWithCounts[subString]?

            - Why subtract by 1?

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
            number_of_anagram_pairs by subStringsWithCounts[subString] - 1!
            That is the direct reflection of: 
            numberOfPairs = previousAmountOfPairs + (numberOfItems - 1)
            In our code!
            '''
    return number_of_anagram_pairs


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, optimal)
    run_dynamic_tests()

