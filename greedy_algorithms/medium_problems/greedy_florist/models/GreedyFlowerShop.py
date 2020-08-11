from math import ceil

from .Friend import Friend


class GreedyFlowerShop:

    def __init__(self, k: int, c: list):
        self.flower_prices: list = c
        self.total: int = 0

    def remove_most_expensive_flower(self):
        most_expensive_flower_price: int = max(self.flower_prices)
        self.flower_prices.remove(most_expensive_flower_price)

    def buy_most_expensive_flower_with(self, customer: Friend):
        most_expensive_flower_price: int = max(self.flower_prices)
        cost = customer.get_flower_cost_at(most_expensive_flower_price)
        self.total += cost

    def flower_prices_is_empty(self) -> bool:
        return len(self.flower_prices) == 0


