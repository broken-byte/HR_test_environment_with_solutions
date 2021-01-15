import os

from test_utilities.time_complexity_file_processing_functions import \
    process_test_file_where_lines_are_int_arrays


current_path = os.path.dirname(__file__)
arrays_0: list = process_test_file_where_lines_are_int_arrays(current_path + "/time_complexity_test_0.txt",
                                                              exclude_index=0)
arrays_1: list = process_test_file_where_lines_are_int_arrays(current_path + "/time_complexity_test_1.txt",
                                                              exclude_index=0)
time_complexity_test_data: dict = {
    "test_time_complexity_0": {
        "params": {
            "a": arrays_0[0],
            "b": arrays_0[1],
            "c": arrays_0[2]
        },
        "expected": 10372982
    },
    "test_time_complexity_1": {
        "params": {
            "a": arrays_1[0],
            "b": arrays_1[1],
            "c": arrays_1[2]
        },
        "expected": 9593177511025
    }
}