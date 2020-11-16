from test_utilities.dynamic_test_creation.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def brute_force_abbreviations(**kwargs) -> str:
    a: str = kwargs["a"]
    b: str = kwargs["b"]
    abbrev: Abbreviation = Abbreviation(a, b)
    if abbrev.can_a_become_b():
        return "YES"
    else:
        return "NO"

    # TODO: Fix test case 0 failure
    # TODO: Fix test case 1 failure


class Abbreviation:
    def __init__(self, a: str, b: str):
        self.a: str = a
        self.b: str = b

    def can_a_become_b(self) -> bool:
        if self.a == self.b:
            return True
        if self.deletion_of_all_lowers_does_fix_a():
            return True
        elif self.capitalization_of_some_lowers_can_fix_a():
            return True
        elif self.b_is_too_large():
            return False
        else:
            return False

    def deletion_of_all_lowers_does_fix_a(self) -> bool:
        temporary_a: str = self.a
        index: int = 0
        while index < len(temporary_a):
            letter: str = temporary_a[index]
            if letter.islower():
                if index == 0:
                    temporary_a = temporary_a[index:]
                else:
                    left: str = temporary_a[:index]
                    right: str = temporary_a[index + 1:]
                    temporary_a = left + right
                    index -= 1
            index += 1
        return temporary_a == self.b

    def capitalization_of_some_lowers_can_fix_a(self):
        for index, letter in enumerate(self.a):
            if index < len(self.b) - 1:
                if letter == self.b[index]:
                    continue
                elif self.capitalization_does_fix_a_at(index):
                    continue
                else:
                    return False

    def capitalization_does_fix_a_at(self, index: int) -> bool:
        return self.a[index].upper() == self.b[index]

    def b_is_too_large(self) -> bool:
        return len(self.b) > len(self.a)


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


