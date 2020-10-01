import math


def optimized_min_time(machines: list, goal: int) -> int:
    factory_rate: float = 0.0
    for days_per_item_rate in machines:
        item_per_day_rate: float = round(1 / days_per_item_rate, 4)
        factory_rate += item_per_day_rate
    minimum_days_till_goal: float = goal / factory_rate
    whole_days_till_goal: int = int(minimum_days_till_goal)
    return whole_days_till_goal
