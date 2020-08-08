

def fraudulentNotifications(expenditure: list, d: int) -> int:
    '''
    Complete the function activityNotifications in the editor below. It must return an integer representing the number of client notifications.

    activityNotifications has the following parameter(s):

    expenditure: an array of integers representing daily expenditures
    d: an integer, the lookback days for median spending
        - Time Complexity: O(n)
    '''
    notifications = 0
    countSortList = [0] * 201
    expenditureLength = len(expenditure)
    rightCursor = d
    leftCursor = 0
    for index in range(leftCursor, rightCursor):
        countSortList[expenditure[index]] += 1
    while rightCursor < expenditureLength:
        median = getMedian(countSortList, d)
        if expenditure[rightCursor] >= median * 2:
            notifications += 1
        countSortList[expenditure[leftCursor]] -= 1
        countSortList[expenditure[rightCursor]] += 1
        # Move queue window forward
        leftCursor += 1
        rightCursor += 1

    return notifications
         
def getMedian(countSortList: list, d: int) -> int:
    '''
    Given a counting sort list and the number
    of previous days, returns the median in the 
    counting sort list. 
    '''
    if d % 2 == 0:
        medianIndex = int(d / 2)
    else: 
        medianIndex = int(d / 2) + 1
    count = 0
    left = 0
    right = 0
    while count < medianIndex:
        count += countSortList[left]
        left += 1
    # This is to place the cursors around the median location (for both even and odd case)
    right = left
    left -= 1
    if d % 2 != 0 or count > medianIndex:
        return left
    else:
        while countSortList[right] == 0:
            right += 1
        return (left + right) / 2

def main():

    tests =[

        [2, 3, 4, 2, 3, 6, 8, 4, 5],

        [1, 2, 3, 4, 4],

        [10, 20, 30, 40, 50]
    ] 

    testDs = [5, 4, 3]

    print(fraudulentNotifications(tests[2], testDs[2]))

if __name__ == "__main__":
    main()