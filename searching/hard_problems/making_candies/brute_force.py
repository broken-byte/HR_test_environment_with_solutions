from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from searching.hard_problems.making_candies.test_resources.functionality_test_data import functionality_test_data


def brute_force(m: int, w: int, p: int, n: int) -> int:
    candy_factory: CandyFactory = CandyFactory(m, w, p, n)
    return candy_factory.minimum_time_to_meet_goal()
# TODO: Currently not working, will return to this. The test cases run correctly though :)


class CandyFactory:

    def __init__(self, machines: int, workers: int, price_per_unit: int, goal: int):
        self.machines: int = machines
        self.workers: int = workers
        self.price_per_worker: int = price_per_unit
        self.price_per_machine: int = price_per_unit
        self.goal: int = goal
        self.candies: int = 0

    def minimum_time_to_meet_goal(self):
        self.make_candies()
        self.buy_machines(self.candies)
        days_to_goal: int = self.get_days_to_goal()
        return days_to_goal

    def make_candies(self):
        self.candies += self.machines * self.candies

    def buy_machines(self, amount: int, price: int):
        self.candies -= price * amount
        self.machines += amount

    def get_days_to_goal(self):
        return self.goal // self.workers * self.machines

    def hire_workers(self, amount: int, price: int):
        self.candies -= price * amount
        self.workers += amount


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
