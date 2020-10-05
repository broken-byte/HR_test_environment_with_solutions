

class FactoryFloor:

    def __init__(self, machines: list, goal: int):
        self.sorted_machines: list = sorted(machines)
        self.number_of_machines: int = len(machines)
        self.goal: int = goal
        self.high_bound: int = 0
        self.low_bound: int = 0

    def get_minimum_time_required_to_meet_goal(self) -> int:
        self.set_worst_case_efficiency_as_initial_high_bound()
        self.set_best_case_efficiency_as_initial_low_bound()
        self.binary_search_for_best_possible_efficiency()
        return self.low_bound

    def set_worst_case_efficiency_as_initial_high_bound(self):
        worst_performing_machine: int = self.sorted_machines[-1]
        self.high_bound: int = int(self.goal // (self.number_of_machines/worst_performing_machine))

    def set_best_case_efficiency_as_initial_low_bound(self):
        best_performing_machine: int = self.sorted_machines[0]
        self.low_bound: int = int(self.goal // (self.number_of_machines/best_performing_machine))

    def binary_search_for_best_possible_efficiency(self):
        while self.low_bound < self.high_bound:
            middle_number_of_days: int = (self.high_bound + self.low_bound) // 2
            middle_number_of_items_produced: int = self.number_of_items_produced_given(middle_number_of_days)
            if middle_number_of_items_produced >= self.goal:
                self.high_bound = middle_number_of_days
            else:
                self.low_bound = middle_number_of_days + 1

    def number_of_items_produced_given(self, number_of_days) -> int:
        sum_of_rates: int = 0
        for machine_rate in self.sorted_machines:
            sum_of_rates += number_of_days//machine_rate
        return sum_of_rates
