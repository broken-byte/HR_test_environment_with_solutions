

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "machines": [2, 3],
            "goal": 5,
        },
        "expected": 6
    },
    "test_1": {
        "params": {
            "machines": [1, 3, 4],
            "goal": 10,
        },
        "expected": 7
    },
    "test_2": {
        "params": {
            "machines": [4, 5, 6],
            "goal": 12,
        },
        "expected": 20
    },
    "test_3": {
        "params": {
            "machines": [2, 3, 2],
            "goal": 10,
        },
        "expected": 8
    },
    "test_4": {
        "params": {
            "machines": [63, 2, 26, 59, 16, 55, 99, 21, 98, 65],
            "goal": 56,
        },
        "expected": 82
    },
}
