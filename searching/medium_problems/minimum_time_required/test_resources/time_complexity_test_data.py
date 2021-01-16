import os

from test_utilities.time_complexity_file_processing_functions import \
    process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)


time_complexity_test_data: dict = {
    "test_0": {
        "params": {
            "machines": process_test_file_where_single_line_is_an_int_array(current_path + "/time_complexity_test_0.txt"),
            "goal": 927,
        },
        "expected": 45261
    },
    "test_1": {
        "params": {
            "machines": process_test_file_where_single_line_is_an_int_array(current_path + "/time_complexity_test_1.txt"),
            "goal": 232897690,
        },
        "expected": 1340828872701
    },
    "test_2": {
        "params": {
            "machines": process_test_file_where_single_line_is_an_int_array(current_path + "/time_complexity_test_2.txt"),
            "goal": 1667,
        },
        "expected": 154
    }
}
