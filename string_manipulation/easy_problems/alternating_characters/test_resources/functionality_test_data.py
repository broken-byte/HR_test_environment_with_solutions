

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "s": "ABABABAB",
        },
        "expected": 0
    },
    "test_1": {
        "params": {
            "s": "BABABA",
        },
        "expected": 0
    },
    "test_2": {
        "params": {
            "s": "AAAA",
        },
        "expected": 3
    },
    "test_3": {
        "params": {
            "s": "BBBBB"
        },
        "expected": 4
    },
    "test_4": {
        "params": {
            "s": "AAABBBAABB",
        },
        "expected": 6
    }
}
