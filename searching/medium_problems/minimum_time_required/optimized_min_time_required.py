from searching.medium_problems.minimum_time_required.classes.FactoryFloor import FactoryFloor


def optimized_min_time(machines: list, goal: int) -> int:
    factory_floor = FactoryFloor(machines, goal)
    minimum_time_required: int = factory_floor.get_minimum_time_required_to_meet_goal()
    return minimum_time_required

