from test_utilities.dynamic_test_creation.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from test_utilities.test_variables import test_suite_separation_line
from arrays.medium_problems.minimum_swaps.test_resources.functionality_test_data import functionality_test_data


def min_swaps(**kwargs):
    a: list = kwargs["a"]
    # Initialize variables for the solution and the list length
    minSwaps = 0
    n = len(a)

    # Bool list of size n so that we know which elements we've visited
    checked = [False] * n

    # Dictionary of item -> index pairs from the sorted version of A
    Asort_dict = {}

    # Feeding sorted elements as key, value pairs into Asort_dict where key = value, value = index
    for i, x in enumerate(sorted(a)):
        Asort_dict[x] = i

    # Master loop to iterate through the original list and find cycles within
    for i, x in enumerate(a):

        # We have checked this value via cycle loop below, move on
        if checked[i]:
            continue

        # Initalize cycle count
        cycle_count = 0

        # The root is the value that if we encounter again, indicates the end of our cycle, breaking our cycle loop
        root = x

        # The variable that will hold the current node we are on in our list implemented graph
        traveler = x

        # Since we are exploring our cycle starting at i, we have checked it!
        checked[i] = True

        # The cycle loop that will follow through the nodes in each cycle until it completes and encounters the root value
        while(True):

            # Set the next node to travel to as checked
            checked[Asort_dict[traveler]] = True

            # Set traveler equal to the next node in the graph
            traveler = a[Asort_dict[traveler]]

            # increment the size of the counter by 1
            cycle_count += 1

            # If this activates, we have gone full circle through our cycle, and we break out of the loop
            if traveler == root: break

        # The theory is that the minimum swaps required to sort a series of nodes in a cycle in ascending or descending order is equal to the size of the cycle - 1
        minSwaps += cycle_count - 1

    # Donzo!
    return minSwaps


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, min_swaps)
    run_dynamic_tests()
