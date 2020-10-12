

def brute_force_making_candies(m: int, w: int, p: int, n: int) -> int:
    pass


class CandyFactory:

    def __init__(self, machines: int, workers: int, price_per_unit: int, goal: int):
        self.machines: int = machines
        self.workers: int = workers
        self.price_per_worker: int = price_per_unit
        self.price_per_machine: int = price_per_unit
        self.goal: int = goal
        self.candies: int = 0

    def minimum_time_to_meet_goal(self):
        pass

    def make_candies(self):
        self.candies += self.machines * self.candies

    def buy_machines(self, amount: int, price: int):
        self.candies -= price * amount
        self.machines += amount

    def hire_workers(self, amount: int, price: int):
        self.candies -= price * amount
        self.workers += amount
