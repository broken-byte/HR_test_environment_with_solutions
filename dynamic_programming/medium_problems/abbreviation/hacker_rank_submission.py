

def abbreviation(a: str, b: str) -> str:
    abbreviation_checker: AbbreviationChecker = AbbreviationChecker(a, b)
    if abbreviation_checker.can_make_abbreviation():
        return "YES"
    else:
        return "NO"


class AbbreviationChecker:
    def __init__(self, a: str, b: str):
        self.a: str = a
        self.b: str = b
        self.recursion_level: int = 0
        self.can_abbreviate: bool = False
        self.continue_searching: bool = True

    def can_make_abbreviation(self) -> bool:
        self.search_for_abbreviation(self.a, 0, 0)
        return self.can_abbreviate

    def search_for_abbreviation(self, a: str, index: int, recursion_level: int):
        if a == self.b:
            self.can_abbreviate = True
            self.continue_searching = False
        elif len(a) > len(self.b):
            a_letter: str = a[index]
            b_letter: str = self.b[index] if index < len(self.b) else None
            if self.continue_searching and self.deletion_is_possible(a_letter):
                self.search_for_abbreviation(delete_character_at(index, a), index, recursion_level + 1)
            if self.continue_searching and self.capping_is_possible_and_useful(a_letter, b_letter):
                self.search_for_abbreviation(capitalize_character_at(index, a), index + 1, recursion_level + 1)

    @staticmethod
    def deletion_is_possible(a_letter: str) -> bool:
        return a_letter.islower()

    @staticmethod
    def capping_is_possible_and_useful(a_letter: str, b_letter: str) -> bool:
        return (a_letter.islower() and a_letter.upper() == b_letter) or (a_letter == b_letter)


def capitalize_character_at(index: int, string: str) -> str:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if index == 0:
        return string[index].upper() + string[index + 1:]
    else:
        return string[:index] + string[index].upper() + string[index + 1:]


def delete_character_at(index: int, string: str) -> str:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if index == 0:
        return string[index + 1:]
    else:
        return string[:index] + string[index + 1:]
