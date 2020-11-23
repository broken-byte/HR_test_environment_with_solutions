functionality_test_data: dict = {
        "test_0": {
            "params": {
                "a": "AbcDE",
                "b": "ABDE"
            },
            "expected": "YES"
        },
        "test_1": {
            "params": {
                "a": "daBcd",
                "b": "ABC"
            },
            "expected": "YES"
        },
        "test_2": {
            "params": {
                "a": "Pi",
                "b": "P"
            },
            "expected": "YES"
        },
        "test_3": {
            "params": {
                "a": "AfPZN",
                "b": "APZNC"
            },
            "expected": "NO"
        },
        "test_4": {
            "params": {
                "a": "KXzQ",
                "b": "K"
            },
            "expected": "NO"
        },
    }
