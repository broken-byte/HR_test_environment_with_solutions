from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.triple_sum.test_resources.functionality_test_data import functionality_test_data


def triple_sum(a: list, b: list, c: list) -> int:
    triplet: list = []
    triplets: set = set([])
    for p in a:
        triplet.clear()
        triplet.append(p)
        for q in b:
            if p <= q:  # keep going
                triplet.append(q)
                pass
            else:
                continue  # skip this q
            for r in c:
                if q >= r:
                    triplet.append(r)
                    hash_triplet: tuple = tuple(triplet)
                    if hash_triplet not in triplets:
                        triplets.add(hash_triplet)
                    triplet.pop()
                else:
                    continue
            triplet.pop()  # remove old q
    return len(triplets)


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, triple_sum)
    run_dynamic_tests()
