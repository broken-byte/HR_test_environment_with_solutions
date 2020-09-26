# TODO: Use binary search HOLY FUCK YES


def optimized_triple_sum(a: list, b: list, c: list) -> int:
    triplet: list = []
    triplets: set = set([])
    sorted_a: list = sorted(a)
    sorted_b: list = sorted(b, reverse=True)
    sorted_c: list = sorted(c)
    for p in sorted_a:
        triplet.clear()
        triplet.append(p)
        for q in sorted_b:
            if p <= q:  # keep going
                triplet.append(q)
            else:
                break
            for r in sorted_c:
                if q >= r:
                    triplet.append(r)
                    hash_triplet: tuple = tuple(triplet)
                    if hash_triplet not in triplets:
                        triplets.add(hash_triplet)
                    triplet.pop()
                else:
                    break
            triplet.pop()  # remove old q
    return len(triplets)
