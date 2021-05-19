from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from arrays.medium_problems.new_years_chaos.test_resources.functionality_test_data import functionality_test_data


def minimum_bribes(q: list) -> int:
    """
    Time Complexity: O(n^2)
    """
    queue: list = [position - 1 for position in q]
    total_bribe_count: int = 0

    for absolute_position, person_sticker in enumerate(queue):
        persons_bribe_count: int = person_sticker - absolute_position
        if persons_bribe_count > 2:
            return -1
        for index in range(max(person_sticker-1, 0), absolute_position):
            if queue[index] > person_sticker:
                total_bribe_count += 1
    return total_bribe_count


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, minimum_bribes)
    run_dynamic_tests()

