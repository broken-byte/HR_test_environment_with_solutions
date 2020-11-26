from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from string_manipulation.medium_problems.special_string_again.test_resources.functionality_test_data import \
    functionality_test_data
from string_manipulation.medium_problems.special_string_again.test_resources.time_complexity_test_data import \
    time_complexity_test_data
from tools.iterables.sub_iterables import \
    get_number_of_sub_arrays_in_an_iterable


def substr_count(n: int, s: str)-> int: # O(N)
    """
    Single pass with branch out strategy
        Time Complexity: O(N)
    """
    special_string_count = n  # Every individual character is a special string
    consecutive_character = s[0]  # Buffer for repeating char
    consecutive_character_count = 1
    for index in range(n - 1):
        if s[index + 1] == consecutive_character:  # Check for repeating chars
            consecutive_character_count += 1
        else:
            # Use math formula for # of subs in a string minus each individual
            # character count (already counted that up top)
            nested_special_strings_so_far = get_number_of_sub_arrays_in_an_iterable(consecutive_character_count)
            special_string_count +=  nested_special_strings_so_far - consecutive_character_count
            # Start branching out from first dissimilar character to check if
            # Middle char special string
            number_of_same_characters_on_left = consecutive_character_count
            number_of_same_characers_on_right = 0
            middle_character_index = index + 1
            branch_out_start = middle_character_index + 1
            end_of_right_side_index = middle_character_index + number_of_same_characters_on_left
            for branchout_index in range(branch_out_start, end_of_right_side_index + 1):
                if branchout_index < n and s[branchout_index] == consecutive_character:
                    number_of_same_characers_on_right += 1
                else: break
            # We've found a middle character special string!
            if number_of_same_characters_on_left >= number_of_same_characers_on_right > 0:
                special_string_count += number_of_same_characers_on_right
            # Reset consecutiveCharacter
            consecutive_character = s[index + 1]
            consecutive_character_count = 1
    # Check to see if we've looped through a long chain of consecutive chars
    # Without end
    if consecutive_character_count > 1:
        nested_special_strings_so_far = get_number_of_sub_arrays_in_an_iterable(consecutive_character_count)
        special_string_count += nested_special_strings_so_far - consecutive_character_count

    return special_string_count


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(
        functionality_test_data,
        substr_count, timed=True,
        timeout=1
    )
    run_dynamic_tests()
