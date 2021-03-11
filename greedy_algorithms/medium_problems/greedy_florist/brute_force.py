from math import ceil

from greedy_algorithms.medium_problems.greedy_florist.classes.Friend import Friend
from greedy_algorithms.medium_problems.greedy_florist.classes.GreedyFlowerShop import GreedyFlowerShop
from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from greedy_algorithms.medium_problems.greedy_florist.test_resources.functionality_test_data import \
    functionality_test_data


def brute_force(k: int, c: list) -> int:
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


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()

