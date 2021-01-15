import os

from test_utilities.time_complexity_file_processing_functions import \
    process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)

time_complexity_test_data: dict = {
    "test_time_complexity_0": {
        "params": {
            "k": 11324,
            "arr": process_test_file_where_single_line_is_an_int_array(
                current_path + "/time_complexity_test_0.txt"
            ),
        },
        "expected": 2617
    },
    "test_time_complexity_1": {
        "params": {
            "k": 30244,
            "arr": process_test_file_where_single_line_is_an_int_array(
                current_path + "/time_complexity_test_1.txt"
            ),
        },
        "expected": 3057
    },
}
