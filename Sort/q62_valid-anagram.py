'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
'''

s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = Solution()
print(s.isAnagram(s1, t1))
print(s.isAnagram(s2, t2))