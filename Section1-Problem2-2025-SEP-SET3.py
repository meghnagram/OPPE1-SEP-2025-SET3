
def n_unique_letters_in_exactly_one_of(s1: str, s2: str) -> int:
    '''
    Returns the number of unique letters present in exactly one
    of the two strings (not in both, case insensitive).

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        int: Count of unique letters in the symmetric difference
    '''
    
    return len(set(s1.lower())^set(s2.lower()))


# Number of Unique letters present in exactly one of the two strings
# Write a function n_unique_letters_in_exactly_one_of(s1, s2) that takes two strings as input and returns the number of unique letters that are present in exactly one of the strings but not in both.

# Assume the strings will have only alphabets (both uppercase and lowercase). The letters should be compared in case insensitive manner ('A' and 'a' are considered same).

# Hint: Use set operations to find this.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> n_unique_letters_in_exactly_one_of("APPLE", "plum")
# 4
# "a", "e", "u" and "m" are the characters that are present in exactly one of the strings.


