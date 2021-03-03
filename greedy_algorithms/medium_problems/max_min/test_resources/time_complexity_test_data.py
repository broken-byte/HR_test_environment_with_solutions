import os

from test_utilities.time_complexity_file_processing_functions import process_test_file_where_lines_are_int_elements

current_path = os.path.dirname(__file__)

time_complexity_test_data: dict = {
    "test_0": {
        "params": {
            "k": 2430,
            "arr": process_test_file_where_lines_are_int_elements(
                current_path + "/time_complexity_test_0.txt"
            )
        },
        "expected": 2374
    },
    "test_1": {
        "params": {
            "k": 90000,
            "arr": process_test_file_where_lines_are_int_elements(
                current_path + "/time_complexity_test_1.txt"
            )
        },
        "expected": 89733159
    }
}
