

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "a": "cde",
            "b": "dcf"
        },
        "expected": 2
    },
    "test_1": {
        "params": {
            "a": "bacdc",
            "b": "dcbad"
        },
        "expected": 2
    },
    "test_2": {
        "params": {
            "a": "abcd",
            "b": "abcd"
        },
        "expected": 0
    },
    "test_3": {
        "params": {
            "a": "a",
            "b": "a"
        },
        "expected": 0
    },
}
