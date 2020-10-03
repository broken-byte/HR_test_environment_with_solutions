from math import ceil
# TODO: fix the below so that works


def optimized_min_time(machines: list, goal: int) -> int:
    sorted_machines: list = sorted(machines)
    number_of_machines: int = len(sorted_machines)

    high_bound: float = goal/number_of_machines * sorted_machines[-1]
    low_bound: float = goal/number_of_machines * sorted_machines[0]

    middle_index: int = number_of_machines // 2
    middle_number_of_days: float = (high_bound + low_bound) / 2
    number_of_items_produced: float = number_of_items_produced_given(middle_number_of_days, machines)

    # Binary Search
    if ceil(number_of_items_produced) == ceil(goal):
        return ceil(middle_number_of_days)
    elif number_of_items_produced > goal:
        left: list = machines[:middle_index]
        return optimized_min_time(left, goal)
    elif number_of_items_produced < goal:
        right: list = machines[middle_index:]
        return optimized_min_time(right, goal)


def number_of_items_produced_given(number_of_days, machines_rates: list) -> float:
    sum_of_rates: float = 0.0
    for machines_rate in machines_rates:
        sum_of_rates += number_of_days/machines_rate
    return sum_of_rates

