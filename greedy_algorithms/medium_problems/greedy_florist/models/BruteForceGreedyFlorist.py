from math import ceil

from .Friend import Friend


class BruteForceGreedyFlorist:

    def __init__(self, k: int, c: list):
        self.friends: list = self.create_friend_list_of_size(k)
        self.flower_prices: list = c
        self.number_of_times_friends_need_to_go_through_buy_cycle: int = ceil(len(c) / k)
        self.total: int = 0

    @staticmethod
    def create_friend_list_of_size(k: int):
        friends: list = []
        for _ in range(k):
            friend: Friend = Friend()
            friends.append(friend)
        return friends

    def get_minimum_cost(self) -> int:  # O(n^2)
        """Time Complexity: O(n^2)"""
        for _ in range(self.number_of_times_friends_need_to_go_through_buy_cycle):  # O(n)
            for friend in self.friends:  # O(n)
                self.buy__most_expensive_flower_with(friend)
                self.remove_most_expensive_flower_price()
                if self.flower_prices_is_empty():
                    return self.total

    def remove_most_expensive_flower_price(self):
        most_expensive_flower_price: int = max(self.flower_prices)
        self.flower_prices.remove(most_expensive_flower_price)

    def buy__most_expensive_flower_with(self, friend: Friend):
        most_expensive_flower_price: int = max(self.flower_prices)
        cost = friend.getFlowerCostAt(most_expensive_flower_price)
        self.total += cost

    def flower_prices_is_empty(self) -> bool:
        return len(self.flower_prices) == 0


