'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = ""
Output: 0

Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        def isRepeat(ss: str) -> bool:
            table = {}
            for char in ss:
                if char in table:
                    return True
                else:
                    table[char] = 1
            return False

        maxLen = 0
        windowSize = 1

        for i in range(len(s)):
            while i + windowSize <= len(s):
                if not isRepeat(s[i:i+windowSize]):
                    maxLen = windowSize
                    windowSize += 1
                else:
                    break

        return maxLen

    def lengthOfLongestSubstring2(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                # 이미 등장했던 문자라면 start 갱신
                start = used[char] + 1
            else:
                # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
            
            used[char] = index
        
        return max_length

solution = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = ""
s5 = " "

print(solution.lengthOfLongestSubstring1(s1))
print(solution.lengthOfLongestSubstring1(s2))
print(solution.lengthOfLongestSubstring1(s3))
print(solution.lengthOfLongestSubstring1(s4))
print(solution.lengthOfLongestSubstring1(s5))