
def brute_force_making_candies(m: int, w: int, p: int, n: int) -> int:
    pass
# TODO: Moving on from this problem since its hindering my rate of problem ingestion


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
