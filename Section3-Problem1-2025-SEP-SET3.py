def filter_words(sentence: str, criteria: str) -> set:
    """Return a set of words filtered by the given criteria."""
    
    
    def is_palindrome(w):
        lw = w.lower()
        return lw == lw[::-1]

    def is_balanced(w):
        lw = w.lower()
        vowels = set('aeiou')
        v = sum(1 for ch in lw if ch in vowels)
        c = sum(1 for ch in lw if ch not in vowels)
        return v == c and v + c > 0

    def is_alphabetical(w):
        lw = w.lower()
        letters = [ch for ch in lw if ch.isalpha()]
        return letters == sorted(letters)

    def alphabetical_palindrome(w):
        return is_palindrome(w) and is_alphabetical(w[:len(w)//2 + len(w)%2])

    def balanced_palindrome(w):

        return is_balanced(w) and is_palindrome(w)

    check_map = {
        'palindromes': is_palindrome,
        'balanced': is_balanced,
        'alphabetical': is_alphabetical,
        'alphabetical_palindromes': alphabetical_palindrome,
        'balanced_palindromes': balanced_palindrome,
    }

    checker = check_map.get(criteria)
    if checker is None:
        return set()
    return {w for w in sentence.split() if checker(w)}
    
# Word Filter by Criteria
# You are given a multi-line string that contains words separated by spaces and line breaks.
# Implement a function

# filter_words(sentence: str, criteria: str) -> set[str]
# that returns a set of words that satisfy the given criteria.
# The supported criteria are:

# palindromes - words that read the same forward and backward.
# balanced - words that contain an equal number of vowels (a, e, i, o, u, case-insensitive) and consonants and atleast one alphabet.
# alphabetical - words whose letters appear in non-decreasing alphabetical order (e.g., "abc", "aab").
# alphabetical_palindromes - words that are palindromes and whose first half (including the middle character for odd-length words) is alphabetical.
# balanced_palindromes - words that are balanced and alphabetical.
# The function should be case-insensitive for all checks, but the returned words must keep their original casing.

# If an unknown criteria string is supplied, return an empty set.

# Ignore non alphabetic characters in the sentence.

