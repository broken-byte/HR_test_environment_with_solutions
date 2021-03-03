

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "k": 2,
            "arr": [1, 4, 7, 2],
        },
        "expected": 1
    },
    "test_1": {
        "params": {
            "k": 3,
            "arr": [10, 100, 300, 200, 1000, 20, 30],
        },
        "expected": 20
    },
    "test_2": {
        "params": {
            "k": 4,
            "arr": [1, 2, 3, 4, 10, 20, 30, 40, 100, 200],
        },
        "expected": 3
    },
    "test_3": {
        "params": {
            "k": 2,
            "arr": [1, 2, 1, 2, 1],
        },
        "expected": 0
    },
}


