

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "q": [2, 1, 5, 3, 4]
        },
        "expected": 3
    },
    "test_1": {
        "params": {
            "q": [1, 2, 5, 3, 7, 8, 6, 4]
        },
        "expected": 7
    },
    "test_2": {
        "params": {
            "q": [2, 5, 1, 3, 4]
        },
        "expected": -1
    },
    "test_3": {
        "params": {
            "q": [5, 1, 2, 3, 7, 8, 6, 4]
        },
        "expected": -1
    },
}
