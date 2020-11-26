

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "s": "abc",
        },
        "expected": "YES"
    },
    "test_1": {
        "params": {
            "s": "abcdefghhgfedecba"
        },
        "expected": "YES"
    },
    "test_2": {
        "params": {
            "s": "aabbcd",
        },
        "expected": "NO"
    },
    "test_3": {
        "params": {
            "s": "aabbccddeefghi"
        },
        "expected": "NO"
    }
}
