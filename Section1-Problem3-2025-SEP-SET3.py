
def double_if_even_else_square(n):
    '''
    Given an integer n, return:
      - 2 * n if n is even
      - n ** 2 if n is odd

    Example:
        >>> double_if_even_else_square(8)
        16
        >>> double_if_even_else_square(9)
        81

    Args:
        n (int): Input integer

    Returns:
        int: Result after applying the rule
    '''
    
    
    return 2 * n if n % 2 == 0 else n ** 2
    
# Double if Even Else Square
# Write a function that takes an integer n and:

# doubles it if it is even,
# otherwise returns its square.
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# >>> double_if_even_else_square(8)
# 16
# >>> double_if_even_else_square(9)
# 81

