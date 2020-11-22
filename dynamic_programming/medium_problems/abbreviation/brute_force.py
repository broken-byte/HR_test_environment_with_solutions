from test_utilities.dynamic_test_creation.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests


def brute_force_abbreviations(**kwargs) -> str:
    a: str = kwargs["a"]
    b: str = kwargs["b"]
    abbreviation: Abbreviation = Abbreviation(a, b)
    result: bool = abbreviation.a_can_become_an_abbreviation_of_b()
    print(f"final result: {result}")
    if result:
        return "YES"
    else:
        return "NO"


class Abbreviation:
    def __init__(self, a: str, b: str):
        self.a: str = a
        self.b: str = b
        self.recursion_level: int = 0

    def a_can_become_an_abbreviation_of_b(self) -> bool:
        return self.search_for_abbreviation(self.a, index=0)

    def search_for_abbreviation(self, a: str, index: int) -> bool:
        self.log_recursion(a, index)
        self.recursion_level += 1
        if a == self.b:
            print(f"returning True, we found an abbreviation!")
            return True
        elif index == len(a):
            return False
        a_letter: str = a[index]
        b_letter: str = self.b[index] if index < len(self.b) else None
        if a_letter.upper() == b_letter:
            capitalized_a: str = self.capitalize_character_from_a_at(index, a)
            return self.search_for_abbreviation(capitalized_a, index + 1)
        elif a_letter.islower():
            trimmed_a: str = self.trim_character_from_a_at(index, a)
            return self.search_for_abbreviation(trimmed_a, index)
        else:
            return False

    def log_recursion(self, a: str, index: int):
        logging_message: str = (f"====================\n"
                                f"Recursion depth level: {self.recursion_level}\n"
                                f"index: {index}\n"
                                f"a: {a}\n"
                                f"b: {self.b}")
        print(logging_message)

    @staticmethod
    def capitalize_character_from_a_at(index: int, a: str) -> str:
        if index == 0:
            return a[index].upper() + a[index + 1:]
        else:
            return a[:index] + a[index].upper() + a[index + 1:]

    @staticmethod
    def trim_character_from_a_at(index: int, a: str) -> str:
        if index == 0:
            return a[index + 1:]
        else:
            return a[:index] + a[index + 1:]


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
        "test_4": {
            "params": {
                "a": "KXzQ",
                "b": "K"
            },
            "expected": "NO"
        },
    }
    dynamically_generate_tests(functionality_test_data, brute_force_abbreviations)
    run_dynamic_tests()
