import os

from test_utilities.time_complexity_file_processing_functions import process_test_file_where_lines_are_int_arrays

current_path = os.path.dirname(__file__)

time_complexity_test_data = {
    "test_time_complexity_0": {
        "params": {
            "k": 99,
            "contests": process_test_file_where_lines_are_int_arrays(
                current_path + "/time_complexity_test_0.txt",
                exclude_index=0,
            )
        },
        "expected": 494906
    }
}
