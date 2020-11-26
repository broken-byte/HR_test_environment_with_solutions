from math import ceil, floor
from typing import List

from sorting.medium_problems.fraudulent_activity.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def fraudulent_notifications(expenditure: list, d: int) -> int:
    number_of_fraudulent_transaction_notifications: int = 0
    expenditure_queue: ExpenditureQueue = ExpenditureQueue(d)
    for e in expenditure:
        if expenditure_queue.is_at_capacity():
            if expenditure_queue.is_fraudulent_transaction(e):
                number_of_fraudulent_transaction_notifications += 1
        expenditure_queue.add_expenditure(e)
    return number_of_fraudulent_transaction_notifications


class ExpenditureQueue:
    """
    The solution to this problem IF the maximum 
    daily expenditure is unknown, which disallows a 
    counting sort approach. However, it is known so whoops :)
    """
    def __init__(self, queue_limit: int):
        self.queue: list = []
        self.max_value: int = 0
        self.queue_median: int = 0
        self.queue_limit: int = queue_limit
        self.has_been_sorted_before: bool = False

    def is_fraudulent_transaction(self, expenditure: int) -> bool:
        if expenditure >= self.queue_median * 2:
            return True
        else:
            return False

    def add_expenditure(self, expenditure: int):
        if expenditure > self.max_value:
            self.max_value = expenditure
        if self.is_at_capacity():
            self.remove_last()
            # No sorting (expensive) needed if this is the case
            if expenditure >= self.queue[-1]:
                self.queue.append(expenditure)
                self.set_queue_median()
            # No sorting (expensive) needed if this is the case
            elif expenditure <= self.queue[0]:
                self.queue.insert(0, expenditure)
                self.set_queue_median()
            # Sorting is needed
            else:
                self.queue.append(expenditure)
                self.count_sort()
                self.set_queue_median()
        else:
            self.queue.append(expenditure)
            # This is to catch the case where the queue is at capacity for the first time and not yet sorted
            if self.is_at_capacity():
                self.count_sort()
                self.set_queue_median()

    def remove_last(self):
        del self.queue[0]

    def is_at_capacity(self) -> bool:
        if len(self.queue) == self.queue_limit:
            return True
        else:
            return False

    def set_queue_median(self):
        n = len(self.queue)
        middle = n / 2
        middle_index1: int = 0
        middle_index2: int = 0
        if n % 2 == 0:
            middle_index1 = floor(middle)
            middle_index2 = ceil(middle)
            median = (self.queue[middle_index1] + self.queue[middle_index2]) / 2

            self.queue_median = median
        else:
            middle = floor(middle)
            self.queue_median = self.queue[middle]

    def count_sort(self):
        count_array: List[int] = [0] * (self.max_value + 1)
        for number in self.queue:
            count_array[number] += 1
        self.queue.clear()
        for index, count in enumerate(count_array):
            for _ in range(count):
                self.queue.append(index)
        self.has_been_sorted_before = True


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications)
    run_dynamic_tests()

