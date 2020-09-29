from searching.medium_problems.triple_sum.classes.TripletCounter import TripletCounter


def optimized_triple_sum(a: list, b: list, c: list) -> int:  # O(b*[log(a) + log(c)])
    triplet_counter = TripletCounter(a, b, c)
    triplet_count: int = triplet_counter.count_triplets()
    return triplet_count





