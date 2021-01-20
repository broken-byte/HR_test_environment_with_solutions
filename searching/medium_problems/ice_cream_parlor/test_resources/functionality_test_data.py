

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "trips": [
                {
                    "money": 5,
                    "cost": [2, 1, 3, 5, 6]
                }
            ],
        },
        "expected": [
                [1, 3]
            ]
    },
    "test_1": {
        "params": {
            "trips": [
                {
                    "money": 4,
                    "cost": [1, 4, 5, 3, 2]
                },
                {
                    "money": 4,
                    "cost": [2, 2, 4, 3]
                }
            ],
        },
        "expected": [
                [1, 4],
                [1, 2]
            ]
    },
    "test_2": {
        "params": {
            "trips": [
                {
                    "money": 5,
                    "cost": [1, 2, 3, 5, 6]
                }
            ],
        },
        "expected":  [
                [2, 3]
            ]
    },
    "test_3": {
        "params": {
            "trips": [
                {
                    "money": 8,
                    "cost": [4, 3, 2, 5, 7]
                },
                {
                    "money": 12,
                    "cost": [7, 2, 5, 4, 11]
                }
            ],
        },
        "expected": [
                [2, 4],
                [1, 3]
            ]
    }
}
