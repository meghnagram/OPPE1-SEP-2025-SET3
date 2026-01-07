

n = int(input())
words = [
    word
    for _ in range(n)
    for word in input().split()
]

odd_pal = even_pal = odd_norm = even_norm = 0

for w in words:
    length = len(w)
    is_pal = w == w[::-1]
    if length % 2 == 1:          # odd length
        if is_pal:
            odd_pal += 1
        else:
            odd_norm += 1
    else:                        # even length
        if is_pal:
            even_pal += 1
        else:
            even_norm += 1

print(odd_pal, even_pal, odd_norm, even_norm)

# Count Word Types by Length and Palindrome Property
# You are given a collection of words separated by whitespace over one or more lines.
# For each word you have to determine

# whether its length is odd or even
# whether it is a palindrome (the word reads the same forwards and backwards)
# Based on these two properties each word belongs to exactly one of the following four categories:

# Odd palindrome - odd length and a palindrome
# Even palindrome - even length and a palindrome
# Odd normal - odd length but not a palindrome
# Even normal - even length but not a palindrome
# Your task is to count how many words fall into each category and output the four counts.

# NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

# Input Format

# First line will contain the number of lines n
# Next n lines will contain the words. Each line contains zero or more words separated by whitespace.
# All words contain only ASCII letters (a-z and A-Z) and are non-empty.
# Output Format

# Print four integers separated by a single space in the following order:

# odd_palindrome_count even_palindrome_count odd_normal_count even_normal_count
# Example

# Input

# 2
# radar level hello world
# noon deed test
# Output

# 2 2 2 1
# Explanation:

# | Word  | Length | Palindrome | Category        |
# | ----- | ------ | ---------- | --------------- |
# | radar | 5      | Yes        | Odd palindrome  |
# | level | 5      | Yes        | Odd palindrome  |
# | hello | 5      | No         | Odd normal      |
# | world | 5      | No         | Odd normal      |
# | noon  | 4      | Yes        | Even palindrome |
# | deed  | 4      | Yes        | Even palindrome |
# | test  | 4      | No         | Even normal     |

