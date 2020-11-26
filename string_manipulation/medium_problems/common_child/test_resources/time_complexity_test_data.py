import os

from test_utilities.time_complexity_file_processing_functions import process_test_file_where_lines_are_str_elements

current_path = os.path.dirname(__file__)
test_data_0: list = process_test_file_where_lines_are_str_elements(current_path + "/time_complexity_test_0.txt")

time_complexity_test_data: dict = {
    "test_time_complexity_0": {
        "params": {
            "s1": test_data_0[0],
            "s2": test_data_0[1]
        },
        "expected": 1417
    }
}
