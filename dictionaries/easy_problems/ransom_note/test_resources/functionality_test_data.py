

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "magazine": ["give", "me", "one", "grand", "today", "night"],
            "note": ["give", "one", "grand", "today"]
        },
        "expected": "Yes"
    },
    "test_1": {
        "params": {
            "magazine": ["two", "times", "three", "is", "not", "four"],
            "note": ["two" "times" "two" "is" "four"]
        },
        "expected": "No"
    },
    "test_2": {
        "params": {
            "magazine": ["ive" "got" "a" "lovely" "bunch" "of" "coconuts"],
            "note": ["ive", "got", "some", "coconuts"]
        },
        "expected": "No"
    },
}
