

def what_flavors(trips: list) -> list:
    flavor_pairs: list = []
    for trip in trips:
        money: int = trip["money"]
        cost: list = trip["cost"]
        distinct_ice_cream_flavors: list = get_optimal_ice_cream_purchases(money, cost)
        flavor_pairs.append(distinct_ice_cream_flavors)
    return flavor_pairs


def get_optimal_ice_cream_purchases(money: int, cost: list) -> list:
    hash_table: dict = {}
    optimal_flavor_choices: list = []
    for index, ice_cream_price in enumerate(cost):
        difference: int = money - ice_cream_price
        if difference in hash_table:
            optimal_flavor_choices.append(hash_table[difference])
            optimal_flavor_choices.append(index + 1)
            return sorted(optimal_flavor_choices)
        hash_table[ice_cream_price] = index + 1
