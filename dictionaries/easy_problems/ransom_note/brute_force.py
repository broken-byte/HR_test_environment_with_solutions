from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from dictionaries.easy_problems.ransom_note.test_resources.functionality_test_data import functionality_test_data


def check_magazine(magazine, note):
    magazine_map = {}
    for word in magazine:
        if word in magazine_map:
            magazine_map[word] += 1
        else:
            magazine_map[word] = 1
    for word in note:
        if word not in magazine_map:
            return "No"
        elif magazine_map[word] == 0:
            return "No"
        else:
            magazine_map[word] -= 1
    return "Yes"


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, check_magazine)
    run_dynamic_tests()
