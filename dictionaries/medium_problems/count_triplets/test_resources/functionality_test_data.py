

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "array_of_numbers": [1, 4, 16, 64],
            "ratio": 4
        },
        "expected": 2
    },
    "test_1": {
        "params": {
            "array_of_numbers": [1, 3, 9, 9, 27, 81],
            "ratio": 3
        },
        "expected": 6
    },
    "test_2": {
        "params": {
            "array_of_numbers": [1, 2, 2, 4],
            "ratio": 2
        },
        "expected": 2
    },
    "test_3": {
        "params": {
            "array_of_numbers": [1, 5, 5, 25, 125],
            "ratio": 5
        },
        "expected": 4
    },
}
