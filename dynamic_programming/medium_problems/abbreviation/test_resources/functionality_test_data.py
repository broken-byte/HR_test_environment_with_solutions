functionality_test_data: dict = {
    "test_0": {
        "params": {
            "a": "abaaA",
            "b": "AA"
        },
        "expected": "YES"
    },
    "test_1": {
        "params": {
            "a": "AbcDE",
            "b": "ABDE"
        },
        "expected": "YES"
    },
    "test_2": {
        "params": {
            "a": "daBcd",
            "b": "ABC"
        },
        "expected": "YES"
    },
    "test_3": {
        "params": {
            "a": "Pi",
            "b": "P"
        },
        "expected": "YES"
    },
    "test_4": {
        "params": {
            "a": "AfPZN",
            "b": "APZNC"
        },
        "expected": "NO"
    },
    "test_5": {
        "params": {
            "a": "KXzQ",
            "b": "K"
        },
        "expected": "NO"
    },
    "test_6": {
        "params": {
            "a": "beFgH",
            "b": "EFH"
        },
        "expected": "YES"
    },
    "test_7": {
        "params": {
            "a": "beFgH",
            "b": "EFG"
        },
        "expected": "NO"
    },
}
