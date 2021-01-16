from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.minimum_time_required.tests.functionality_test_data import functionality_test_data


def min_time(machines: list, goal: int) -> int:
    factory_floor: list = []
    for machine_production_rate in machines:
        machine = Machine(machine_production_rate)
        factory_floor.append(machine)
    items_produced: int = 0
    days_passed: int = 0
    while items_produced < goal:
        total_items_produced_today: int = 0
        for machine in factory_floor:
            machine.work_one_day()
        for machine in factory_floor:
            items_produced_by_machine: int = machine.give_produced_items()
            total_items_produced_today += items_produced_by_machine
        items_produced += total_items_produced_today
        days_passed += 1
    return days_passed


class Machine:

    def __init__(self, production_rate_per_item: int):
        self.production_rate_per_item: int = production_rate_per_item
        self.items_produced: int = 0
        self.days_worked_since_item_finished = 0

    def work_one_day(self):
        self.days_worked_since_item_finished += 1
        if self.days_worked_since_item_finished == self.production_rate_per_item:
            self.items_produced += 1
            self.days_worked_since_item_finished = 0

    def give_produced_items(self):
        collected_items: int = 0
        if self.items_produced != 0:
            collected_items = self.items_produced
        self.items_produced = 0
        return collected_items


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, min_time)
    run_dynamic_tests()
