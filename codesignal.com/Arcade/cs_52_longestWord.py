'''
2022/05/06

Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".
'''

import re
def solution(text):
    return sorted(re.split("[^a-zA-Z]+", text), key=len)[-1]


print(solution("Ready, steady, go!")) # steady
print(solution("Ready[[[, steady, go!")) # steady
print(solution("ABCd")) # ABCd
print(solution("To be or not to be")) # not
print(solution("You are the best!!!!!!!!!!!! CodeFighter ever!")) # CodeFighter
