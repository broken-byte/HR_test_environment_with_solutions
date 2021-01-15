

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "a": [1, 3, 5],
            "b": [2, 3],
            "c": [1, 2, 3],
        },
        "expected": 8
    },
    "test_1": {
        "params" : {
            "a": [1, 4, 5],
            "b": [2, 3, 3],
            "c": [1, 2, 3],
        },
        "expected": 5
    },
    "test_2": {
        "params": {
            "a": [1, 3, 5, 7],
            "b": [5, 7, 9],
            "c": [7, 9, 11, 13]
        },
        "expected": 12
    },
    "test_3": {
        "params": {
            "a": [3, 5, 7],
            "b": [3, 6],
            "c": [4, 6, 9],
        },
        "expected": 4
    },
}
