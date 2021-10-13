'''
Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false
'''
from collections import deque
import time
import re
from typing import Deque

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        # using list
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        # using deque
        strs: Deque = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
    
    def isPalindrome3(self, s: str) -> bool:
        # using slicing
        s = s.lower()
        s = re.sub('[^0-9a-z]', '', s)
        return s == s[::-1]


solution = Solution()
s = "A man, a plan, a canal: Panama"

result = solution.isPalindrome1(s)
print(s, " : ", result)

result = solution.isPalindrome2(s)
print(s, " : ", result)

result = solution.isPalindrome3(s)
print(s, " : ", result)

# s = "race a car"
# print(s, " : ", solution.isPalindrome(s))
