from searching.medium_problems.minimum_time_required.classes.FactoryFloor import \
    FactoryFloor
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.minimum_time_required.test_resources.functionality_test_data import \
    functionality_test_data
from searching.medium_problems.minimum_time_required.test_resources.time_complexity_test_data import \
    time_complexity_test_data


def min_time(machines: list, goal: int) -> int:
    factory_floor = FactoryFloor(machines, goal)
    minimum_time_required: int = factory_floor.get_minimum_time_required_to_meet_goal()
    return minimum_time_required


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, min_time, timed=True)
    run_dynamic_tests()
