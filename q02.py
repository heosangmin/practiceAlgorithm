'''
q02. 문자열 뒤집기
'''

from typing import List


def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    # or
    # s.reverse()

s = ['H','a','n','n','a','h']
print(s)
reverseString(s)
print(s)