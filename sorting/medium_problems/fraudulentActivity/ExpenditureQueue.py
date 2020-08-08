from math import ceil, floor


class ExpenditureQueue:
    '''
    The solution to this problem IF the maximum 
    daily expenditure is unknown, which disallows a 
    counting sort approach.
    '''
    queue = []
    queueLimit = 0
    maxValue = 0
    queueMedian = 0
    hasBeenSortedBefore = False
    
    def __init__(self, queueLimit: int):
        self.queueLimit = queueLimit

    def hasFraudulentTransaction(self, expenditure: int) -> bool:
        if expenditure >= self.queueMedian * 2: 
            return True
        else: 
            return False

    def addExpenditure(self, expenditure: int):
        if expenditure > self.maxValue: 
            self.maxValue = expenditure
        if self.isAtCapacity():
            self.removeLast()
            # No sorting (expensive) needed if this is the case
            if expenditure >= self.queue[-1]:
                self.queue.append(expenditure)
                self.setQueueMedian()
            # No sorting (expensive) needed if this is the case
            elif expenditure <= self.queue[0]:
                self.queue.insert(0, expenditure)
                self.setQueueMedian()
            # Sorting is needed
            else: 
                self.queue.append(expenditure)
                self.countSort()
                self.setQueueMedian()
        else: 
            self.queue.append(expenditure)
            # This is to catch the case where the queue is at capacity for the first time and not yet sorted
            if self.isAtCapacity():
                self.countSort()
                self.setQueueMedian()

    def removeLast(self):
        del self.queue[0]
    
    def isAtCapacity(self) -> bool:
        if len(self.queue) == self.queueLimit: 
            return True
        else: 
            return False

    def setQueueMedian(self):
        n = len(self.queue)
        middle = n / 2
        middleIndex1 = 0
        middleIndex2 = 0
        if n % 2 == 0:
            middleIndex1 = floor(middle)
            middleIndex2 = ceil(middle)
            median =  (self.queue[middleIndex1] + self.queue[middleIndex2]) / 2
            
            self.queueMedian = median
        else: 
            middle = floor(middle)
            self.queueMedian = self.queue[middle]
     
    def countSort(self):
        countArray = [0] * (self.maxValue + 1)
        for number in self.queue:
            countArray[number] += 1
        self.queue.clear()
        for index, count in enumerate(countArray):
            for _ in range(count):
                self.queue.append(index)
        self.hasBeenSortedBefore = True