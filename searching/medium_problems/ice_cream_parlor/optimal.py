from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.ice_cream_parlor.test_resources.functionality_test_data import functionality_test_data


def optimal(trips: list) -> list:
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


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
