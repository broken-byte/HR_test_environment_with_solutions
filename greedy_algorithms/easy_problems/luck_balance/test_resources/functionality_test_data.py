

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "k": 2,
            "contests": [
                [5, 1],
                [1, 1],
                [4, 0],
            ],
        },
        "expected": 10
    },
    "test_1": {
        "params": {
            "k": 1,
            "contests": [
                [5, 1],
                [1, 1],
                [4, 0],
            ],
        },
        "expected": 8
    },
    "test_2": {
        "params": {
            "k": 3,
            "contests": [
                [5, 1],
                [2, 1],
                [1, 1],
                [8, 1],
                [10, 0],
                [5, 0]
            ],
        },
        "expected": 29
    },
    "test_3": {
        "params": {
            "k": 5,
            "contests": [
                [13, 1],
                [10, 1],
                [9, 1],
                [8, 1],
                [13, 1],
                [12, 1],
                [18, 1],
                [13, 1]
            ],
        },
        "expected": 42
    },
    "test_4": {
        "params": {
            "k": 2,
            "contests": [
                [5, 1],
                [4, 0],
                [6, 1],
                [2, 1],
                [8, 0]
            ],
        },
        "expected": 21
    }
}
