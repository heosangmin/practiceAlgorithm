'''
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.
'''

import re
def solution(inputString):
    l = list(map(int, re.findall("\d+", inputString)))
    return sum(l) if len(l) > 0 else 0

print(solution(inputString = "2 apples, 12 oranges")) # 14
print(solution(inputString = "text only")) # 0

'''
문자열에서 숫자만 뽑아서 합하면 되는 건가?
'''