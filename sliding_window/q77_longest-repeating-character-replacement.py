'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''

import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        문자열 s에서 같은 문자로만 이루어진 가장 긴 부분 문자열의 길이를 구하되 최대 k번 만큼 문자를 변경할 수 있다.
        책에서는 k번 만큼의 변경이라고만 써 있어서 무조건 k번의 변경을 해야한다고 착각하기 쉽다.(예전에 다른 문제들에서도 그러더니)

        책의 풀이에 의하면 투 포인터, 슬라이딩 윈도우, Counter를 모두 이용해야 한다.
        최종 결과는 오른쪽 포인터에서 왼쪽 포인터 위치를 뺀 다음, 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이
        k와 같을 수 있는 수 중 가장 큰 최댓값이라 정의할 수 있다.

        max(right) - min(left) - max_char_n == k

        '''
        left = right = 0
        counts = collections.Counter()

        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1

            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
            
        return right - left

sol = Solution()

s = "ABAB"
k = 2
print(s, k, sol.characterReplacement(s, k))

s = "AABABBA"
k = 1
print(s, k, sol.characterReplacement(s, k))
