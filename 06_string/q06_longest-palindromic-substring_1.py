'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "babad"
Output: "bab"

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(0, len(s) - 1):
            result = max(result, expand(i,i+2), expand(i,i+1), key=len)

        return result


solution = Solution()

s = "babad"
s = "cbbd"
s = "a"
s = "ac"
s = "123454321"
print(solution.longestPalindrome(s))

