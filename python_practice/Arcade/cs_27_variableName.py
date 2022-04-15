'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
'''
import re

def solution(name):
    return re.match("^[a-zA-Z_]\w*$", name) != None

# 이건 대박이다.
# return name.isidentifier()

name = "var_1__Int"
print(solution(name)) # T
name = "qq-q"
print(solution(name)) # F
name = "2w2"
print(solution(name)) # F