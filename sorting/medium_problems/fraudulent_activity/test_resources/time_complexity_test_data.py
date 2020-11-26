import os

from test_utilities.time_complexity_file_processing_functions import \
    process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)

time_complexity_test_data: dict = {
    "test_time_complexity_0": {
        "params": {
            "expenditure": process_test_file_where_single_line_is_an_int_array(current_path +
                                                                               "/time_complexity_test_0.txt"),
            "d": 10000
        },
        "expected": 633
    },
}
