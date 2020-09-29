import bisect


def optimized_triple_sum(a: list, b: list, c: list) -> int:  # O(b*[log(a) + log(c)])
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
        index_of_q_in_a: int = self.find_index_of_where_q_would_fit_whilst_maintaining_order_in_a(q)
        index_of_q_in_c: int = self.find_index_of_where_q_would_fit_whilst_maintaining_order_in_c(q)
        if self.triplets_are_possible_given(index_of_q_in_a, index_of_q_in_c):
            triplets: int = self.get_all_possible_combinations_of_valid_triplets_given(index_of_q_in_a, index_of_q_in_c)
            self.count += triplets

    def find_index_of_where_q_would_fit_whilst_maintaining_order_in_a(self, q: int) -> int:
        return bisect.bisect_right(self.a, q)

    def find_index_of_where_q_would_fit_whilst_maintaining_order_in_c(self, q: int) -> int:
        return bisect.bisect_right(self.c, q)

    @staticmethod
    def triplets_are_possible_given(index_of_q_in_a: int, index_of_q_in_c: int) -> bool:
        return index_of_q_in_a != 0 and index_of_q_in_c != 0

    @staticmethod
    def get_all_possible_combinations_of_valid_triplets_given(index_of_q_in_a: int, index_of_q_in_c: int) -> int:
        return index_of_q_in_a * index_of_q_in_c
