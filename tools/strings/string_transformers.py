

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
