

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "s": "abab",
        },
        "expected": "ab"
    },
    "test_1": {
        "params": {
            "s": "eggegg",
        },
        "expected": "egg"
    },
    "test_2": {
        "params": {
            "s": "abcdefgabcdefg",
        },
        "expected": "agfedcb"
    },
    "test_3": {
        "params": {
            "s": "aeiouuoiea",
        },
        "expected": "aeiou"
    },
}
