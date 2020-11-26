from sorting.medium_problems.fraudulent_activity.test_resources.functionality_test_data import \
    functionality_test_data
from sorting.medium_problems.fraudulent_activity.test_resources.time_complexity_test_data import \
    time_complexity_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def fraudulent_notifications(expenditure: list, d: int) -> int:
    notifications = 0
    count_sort_list = [0] * 201
    expenditure_length = len(expenditure)
    right_cursor = d
    left_cursor = 0
    for index in range(left_cursor, right_cursor):
        count_sort_list[expenditure[index]] += 1
    while right_cursor < expenditure_length:
        median = get_median(count_sort_list, d)
        if expenditure[right_cursor] >= median * 2:
            notifications += 1
        count_sort_list[expenditure[left_cursor]] -= 1
        count_sort_list[expenditure[right_cursor]] += 1
        # Move queue window forward
        left_cursor += 1
        right_cursor += 1

    return notifications


def get_median(count_sort_list: list, d: int) -> int:
    """
    Given a counting sort list and the number
    of previous days, returns the median in the 
    counting sort list. 
    """
    if d % 2 == 0:
        median_index = int(d / 2)
    else: 
        median_index = int(d / 2) + 1
    count = 0
    left = 0
    right = 0
    while count < median_index:
        count += count_sort_list[left]
        left += 1
    # This is to place the cursors around the median location (for both even and odd case)
    right = left
    left -= 1
    if d % 2 != 0 or count > median_index:
        return left
    else:
        while count_sort_list[right] == 0:
            right += 1
        return (left + right) / 2


if __name__ == "__main__":
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications, timed=True, timeout=7)
    run_dynamic_tests()
