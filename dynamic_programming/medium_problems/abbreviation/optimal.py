from test_utilities.dynamic_test_creation.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from test_utilities.test_variables import test_suite_separation_line


def optimal_abbreviations(**kwargs) -> str:
    pass


if __name__ == '__main__':
    functionality_test_data: dict = {
        "test_functionality_0": {
            "params": {
                "a": "AbcDE",
                "b": "ABDE"
            },
            "expected": "YES"
        },
        "test_functionality_1": {
            "params": {
                "a": "daBcd",
                "b": "ABC"
            },
            "expected": "YES"
        },
        "test_functionality_2": {
            "params": {
                "a": "Pi",
                "b": "P"
            },
            "expected": "YES"
        },
        "test_functionality_3": {
            "params": {
                "a": "AfPZN",
                "b": "APZNC"
            },
            "expected": "NO"
        },
    }
    dynamically_generate_tests(functionality_test_data, optimal_abbreviations)
    run_dynamic_tests()
    print(test_suite_separation_line)
    time_complexity_test_data: dict = {
        "test_time_complexity_0": {
            "params": {
                "a": "RDWPJPAMKGRIWAPBZSYWALDBLDOFLWIQPMPLEMCJXKAENTLVYMSJNRJAQQPWAGVcGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDDOFCYWBUCJGbvqlddfazmmohcewjg",
                "b": "RDPJPAMKGRIWAPBZSYWALDBLOFWIQPMPLEMCJXKAENTLVYMJNRJAQQPWAGVGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDOFCYWBUCJG"
            },
            "expected": "NO"
        },
        "test_time_complexity_1": {
            "params": {
                "a": "MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp",
                "b": "MBQEVZP"
            },
            "expected": "NO"
        },
        "test_time_complexity_2": {
            "params": {
                "a": "INVMKSOfsVQByBnCWNKPRFRKMhFRSkNQRBVNTIKNBXRSXdADOSeNDcLWFCERZOLQjEZCEPKXPCYKCVKALNxBADQBFDQUpdqunpelxauyyrwtjpkwoxlrrqbjtxlkvkcajhpqhqeitafcsjxwtttzyhzvh",
                "b": "DINVMKSOVQBBCWNKPRFRKMFRSNQRBVNTIKNBXRSXADOSNDLWFCERZOLQEZCEPKXPCYKCVKALNBADQBFDQU"
            },
            "expected": "YES"
        },
        "test_time_complexity_3": {
            "params": {
                "a": "BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms",
                "b": "BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF"
            },
            "expected": "YES"
        }
    }
    dynamically_generate_tests(time_complexity_test_data, optimal_abbreviations, timed=True, timeout=4)
    run_dynamic_tests()
