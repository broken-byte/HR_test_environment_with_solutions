import bisect

from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.triple_sum.test_resources.functionality_test_data import functionality_test_data
from searching.medium_problems.triple_sum.test_resources.time_complexity_test_data import time_complexity_test_data


def triple_sum(a: list, b: list, c: list) -> int:  # O(b*{log(a) + log(c)})
    triplet_counter = TripletCounter(a, b, c)
    triplet_count: int = triplet_counter.count_triplets()
    return triplet_count


class TripletCounter:

    def __init__(self, a: list, b: list, c: list):
        self.a: list = a
        self.b: list = b
        self.c: list = c
        self.count: int = 0

    def count_triplets(self):
        self.remove_duplicates_from_lists()
        self.sort_lists()
        if self.list_elements_incompatible():
            return 0
        for q in self.b:
            self.find_all_possible_triplets_given(q)
        return self.count

    def remove_duplicates_from_lists(self):
        self.a = list(set(self.a))
        self.b = list(set(self.b))
        self.c = list(set(self.c))

    def sort_lists(self):
        self.a = sorted(self.a)
        self.b = sorted(self.b)
        self.c = sorted(self.c)

    def list_elements_incompatible(self) -> bool:
        return min(self.a) > max(self.b) or max(self.b) < min(self.c)

    def find_all_possible_triplets_given(self, q: int):
        valid_elements_in_a: int = self.find_all_elements_in_array_a_that_are_less_than_or_equal_to(q)
        valid_elements_in_c: int = self.find_all_elements_in_array_c_that_are_less_than_or_equal_to(q)
        if self.triplets_are_possible_given(valid_elements_in_a, valid_elements_in_c):
            all_possible_triplet_combinations: int = valid_elements_in_a * valid_elements_in_c
            self.count += all_possible_triplet_combinations

    def find_all_elements_in_array_a_that_are_less_than_or_equal_to(self, q: int) -> int:
        return bisect.bisect_right(self.a, q)

    def find_all_elements_in_array_c_that_are_less_than_or_equal_to(self, q: int) -> int:
        return bisect.bisect_right(self.c, q)

    @staticmethod
    def triplets_are_possible_given(valid_elements_in_a: int, valid_elements_in_c: int) -> bool:

        return valid_elements_in_a != 0 and valid_elements_in_c != 0


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, triple_sum, timed=True)
    run_dynamic_tests()
