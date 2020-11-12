from test_utilities.dynamic_test_creation.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def brute_force_abbreviations(**kwargs) -> str:
    pass


if __name__ == '__main__':
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
    }
    dynamically_generate_tests(functionality_test_data, brute_force_abbreviations)
    run_dynamic_tests()

