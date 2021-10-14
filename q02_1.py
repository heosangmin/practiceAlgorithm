'''
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # pythonic way
        # s = s.reverse()

        # 2 pointer
        left = 0
        right = len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

s = ["h","e","l","l","o"]
solution = Solution()
solution.reverseString(s)
print(s)