

n = int(input())
print(' '*(2*n-1)+'_')
for i in range(1,n):
    print(' '*(2*(n-i)-1)+'_|'+' '*(4*i-3)+'|_')
print('|'+'_'*(4*n-3)+'|')

# Step Triangle Pattern
# Given a positive integer n print a step triangle pattern with the height of n steps.

# There should not be spaces at the end of the lines.

# NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

# Examples

# Input

# 1
# Output 1

#  _
# |_|
# Input

# 2
# Output 2

#    _
#  _| |_
# |_____|
# Input

# 3
# Output 3

#      _
#    _| |_
#  _|     |_
# |_________|
# Input

# 4
# Output 4

#        _
#      _| |_
#    _|     |_
#  _|         |_
# |_____________|
# Input

# 5
# Output 5

#          _
#        _| |_
#      _|     |_
#    _|         |_
#  _|             |_
# |_________________|
