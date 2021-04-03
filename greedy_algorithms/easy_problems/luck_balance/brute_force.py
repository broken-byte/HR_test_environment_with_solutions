from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, \
    run_dynamic_tests
from greedy_algorithms.easy_problems.luck_balance.test_resources.functionality_test_data import \
    functionality_test_data
from greedy_algorithms.easy_problems.luck_balance.test_resources.time_complexity_test_data import \
    time_complexity_test_data


def brute_force(k: int, contests: list) -> int:
    important_luck, unimportant_luck = filter_contests_into_two_lists(contests)
    max_luck_total: int = 0

    for _ in range(k):
        if len(important_luck) > 0:
            max_luck_total += max(important_luck)
            important_luck.remove(max(important_luck))

    max_luck_total += sum(unimportant_luck) - sum(important_luck)
    return max_luck_total


def filter_contests_into_two_lists(contests: list) -> tuple:
    luck_balance_filter: LuckBalanceFilter = LuckBalanceFilter(contests)
    luck_balance_filter.filter()

    important_luck: list = luck_balance_filter.important_luck_balances
    unimportant_luck: list = luck_balance_filter.unimportant_luck_balances

    return important_luck, unimportant_luck


class LuckBalanceFilter:

    def __init__(self, contests: list):
        self.contests: list = contests
        self.important_luck_balances: list = []
        self.unimportant_luck_balances: list = []

    def filter(self):
        for luck_balance, contest_importance in self.contests:
            if contest_importance == 1:
                self.important_luck_balances.append(luck_balance)
            else:
                self.unimportant_luck_balances.append(luck_balance)


if __name__ == "__main__":
    functionality_test_data.update(time_complexity_test_data)
    print(functionality_test_data)
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
