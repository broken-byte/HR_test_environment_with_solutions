

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "expenditure": [2, 3, 4, 2, 3, 6, 8, 4, 5],
            "d": 5
        },
        "expected": 2
    },
    "test_1": {
        "params": {
            "expenditure": [1, 2, 3, 4, 4],
            "d": 4
        },
        "expected": 0
    },
    "test_2": {
        "params": {
            "expenditure": [10, 20, 30, 40, 50],
            "d": 3
        },
        "expected": 1
    }
}
