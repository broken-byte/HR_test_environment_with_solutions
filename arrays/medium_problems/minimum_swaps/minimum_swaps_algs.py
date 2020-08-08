

def min_swaps(A):
    # Initialize variables for the solution and the list length
    minSwaps = 0
    n = len(A)

    # Bool list of size n so that we know which elements we've visited 
    checked = [False] * n

    # Dictionary of item -> index pairs from the sorted version of A
    Asort_dict = {}

    # Feeding sorted elements as key, value pairs into Asort_dict where key = value, value = index
    for i, x in enumerate(sorted(A)):
        Asort_dict[x] = i
    
    # Master loop to iterate through the original list and find cycles within
    for i, x in enumerate(A):

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
            traveler = A[Asort_dict[traveler]]

            # increment the size of the counter by 1
            cycle_count += 1

            # If this activates, we have gone full circle through our cycle, and we break out of the loop
            if traveler == root: break

        # The theory is that the minimum swaps required to sort a series of nodes in a cycle in ascending or descending order is equal to the size of the cycle - 1
        minSwaps += cycle_count - 1
    
    #Donzo!
    return minSwaps