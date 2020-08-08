
from .models.BruteForceGreedyFlorist import BruteForceGreedyFlorist


def get_minimum_cost_brute_force_approach(k: int, c: list) -> int:
    florist_shop: BruteForceGreedyFlorist = BruteForceGreedyFlorist(k, c)

    for _ in range(florist_shop.number_of_times_friends_need_to_go_through_buy_cycle):  # O(c)
        for friend in florist_shop.friends:  # O(k)
            florist_shop.buy__most_expensive_flower_with(friend)
            florist_shop.remove_most_expensive_flower_price()

            if florist_shop.flower_prices_is_empty():
                return florist_shop.total


