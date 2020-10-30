

def what_flavors(trips: list) -> list:
    flavor_pairs: list = []
    for trip in trips:
        money: int = trip["money"]
        cost: list = trip["cost"]
        distinct_ice_cream_flavors: list = get_optimal_ice_cream_purchases(money, cost)
        flavor_pairs.append(distinct_ice_cream_flavors)
    return flavor_pairs


def get_optimal_ice_cream_purchases(money: int, cost: list) -> list:
    distinct_flavors: list = []
    hashed_flavors: dict = {}
    for i, ice_cream_flavor in enumerate(cost):
        if ice_cream_flavor in hashed_flavors:
            hashed_flavors[ice_cream_flavor] = i + 1
    print(hashed_flavors)
    print(cost)
    for ice_cream_flavor in hashed_flavors.keys():
        difference: int = money - ice_cream_flavor
        if difference in hashed_flavors:
            distinct_flavors.append(hashed_flavors[difference])
            distinct_flavors.append(hashed_flavors[ice_cream_flavor])
            break
    return sorted(distinct_flavors)
