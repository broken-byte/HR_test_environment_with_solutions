

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "s1": "ABCD",
            "s2": "ABDC"
        },
    "expected": 3
    },
    "test_1": {
        "params": {
            "s1": "AA",
            "s2": "BB"
        },
        "expected": 0
    },
    "test_2": {
        "params": {
            "s1": "HARRY",
            "s2": "SALLY"
        },
        "expected": 2
    },
    "test_3": {
        "params": {
            "s1": "SHINCHAN",
            "s2": "NOHARAAA"
        },
        "expected": 3
    },
    "test_4": {
        "params": {
            "s1": "ABCDEF",
            "s2": "FBDAMN"
        },
        "expected": 2
    }
}
