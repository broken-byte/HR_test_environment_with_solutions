
def minimumBribes(q: list) -> int:
    '''
    Prints the minimum number of bribes needed
    to get a given queue, q, to it's final state
    if possible, else prints "Too Chaotic"
        - Time Complexity: O(n^2)
    '''
    queue: list = [position - 1 for position in q]
    totalBribeCount: int = 0

    for absolutePosition, personSticker in enumerate(queue):
        personsBribeCount: int = personSticker - absolutePosition
        if personsBribeCount > 2:
            print('Too chaotic')
            return -1
        for index in range(max(personSticker-1, 0), absolutePosition):
            if queue[index] > personSticker:
                totalBribeCount += 1

    print(totalBribeCount)
    return totalBribeCount


if __name__ == '__main__':
    queue: list = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(queue)
