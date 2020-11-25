from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from dynamic_programming.medium_problems.abbreviation.test_resources.functionality_test_data import \
    functionality_test_data
from tools.strings.string_transformers import delete_character_at, capitalize_character_at
from tools.logging.recursion import log_recursion


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
        log_recursion(self.recursion_level, a=a, b=self.b, index=index)
        self.recursion_level += 1
        if a == self.b:
            print(f"returning True, we found an abbreviation!")
            return True
        elif index == len(a):
            return False
        a_letter: str = a[index]
        b_letter: str = self.b[index] if index < len(self.b) else None
        if a_letter.upper() == b_letter:
            capitalized_a: str = capitalize_character_at(index, a)
            return self.search_for_abbreviation(capitalized_a, index + 1)
        elif a_letter.islower():
            trimmed_a: str = delete_character_at(index, a)
            return self.search_for_abbreviation(trimmed_a, index)
        else:
            return False


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force_abbreviations, timed=True)
    run_dynamic_tests()
