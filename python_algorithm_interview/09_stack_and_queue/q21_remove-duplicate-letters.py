'''
316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
'''

import collections

class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters1(suffix.replace(char,''))
        return ''

    def removeDuplicateLetters2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

s1 = "bcabc"
s2  = "cbacdcbc"
solution = Solution()
print(solution.removeDuplicateLetters1(s1))
print(solution.removeDuplicateLetters1(s2))
print(solution.removeDuplicateLetters2(s1))
print(solution.removeDuplicateLetters2(s2))