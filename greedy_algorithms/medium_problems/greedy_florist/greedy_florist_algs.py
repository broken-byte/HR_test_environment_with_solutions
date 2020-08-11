from math import ceil

from .models.GreedyFlowerShop import GreedyFlowerShop
from .models.Friend import Friend


def get_minimum_cost_brute_force_approach(k: int, c: list) -> int:
    greedy_flower_shop: GreedyFlowerShop = GreedyFlowerShop(k, c)
    friends: list = create_friend_list_of_size(k)
    number_of_friend_passes: int = ceil(len(c) / k)

    for _ in range(number_of_friend_passes):  # O(c/k)
        for friend in friends:  # O(k)
            greedy_flower_shop.buy_most_expensive_flower_with(customer=friend)
            greedy_flower_shop.remove_most_expensive_flower()

            if greedy_flower_shop.flower_prices_is_empty():
                return greedy_flower_shop.total


def create_friend_list_of_size(k: int):
    friends: list = []
    for _ in range(k):
        friend: Friend = Friend()
        friends.append(friend)
    return friends
