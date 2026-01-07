
def repeated_characters(s: str) -> list:
    """Finds characters that appear more than once."""
    
    
    count = {}
    result = []
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] > 1 and char not in result:
            result.append(char)
    return result
    

# Find Characters Appearing More Than Once
# Write a function repeated_characters(s) that returns a list of characters that appear more than once in the given string s.
# The order of characters in the output should match their first appearance in s.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> s = "programming"
# >>> repeated_characters(s)
# ['r', 'g', 'm']
# >>> s = "hello"
# >>> repeated_characters(s)
# ['l']
# >>> s = "abc"
# >>> repeated_characters(s)
# []

