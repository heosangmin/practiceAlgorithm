'''
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false
'''

class Solution:
    def isValid1(self, s: str) -> bool:
        stack = []
        table = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for chr in s:
            if table.get(chr):
                stack.append(chr)
            else:
                if not stack or table.get(stack.pop()) != chr:
                    return False
        if stack:
            return False
        return True

    def isValid2(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

solution = Solution()
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
print(solution.isValid1(s1))
print(solution.isValid1(s2))
print(solution.isValid1(s3))
print(solution.isValid1(s4))
print(solution.isValid2(s1))
print(solution.isValid2(s2))
print(solution.isValid2(s3))
print(solution.isValid2(s4))