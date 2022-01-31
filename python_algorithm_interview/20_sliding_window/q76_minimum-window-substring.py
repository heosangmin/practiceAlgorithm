'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
'''

import collections

class Solution:
    def minWindow_bf(self, s: str, t: str) -> str:
        '''
        모든 윈도우 사이즈로 순차 확인하는 방법
        아마 타임 아웃 에러가 발생할 것이다.
        '''
        def contains(sub_str: str, target_str: str) -> bool:
            for target_chr in target_str:
                if target_chr not in sub_str:
                    return False
            return True

        k = len(t)
        while k <= len(s):
            for i in range(len(s) - k + 1):
                if contains(s[i:i + k], t):
                    return s[i:i + k]
            k += 1
        return ""

    def minWindow_tp(self, s: str, t: str) -> str:
        '''
        슬라이딩 윈도우와 투 포인터를 결합한 방식
        
        타겟 문자들이 모두 포함될 때까지 윈도우를 늘려간다.
            모두 포함될 때, 왼족 포인터가 타겟 문자가 될 때까지 오른쪽으로 옮긴다.(윈도우를 좁힌다)
            왼쪽 포인터를 한 칸 더 전진시킨다.

        하고자 하는 바는 이해 가는데 풀이를 보면 카운터 컬렉션을 사용하거나
        left, right 포인터 외에 start, end를 쓰는 것 까지 도출하기가 쉽지 않다.
        '''
        need = collections.Counter(t) # 해당 문자의 값이 0이라는 건 윈도우에 포함되었다는 뜻. -1이라면 윈도우에 들어왔지만 불필요한 문자라는 뜻.
        missing = len(t) # 0이 된다는 건 필요한 문자가 모두 윈도우에 들어왔다는 뜻
        left = start = end = 0 # left, right는 확인을 위한 포인터이고 start, end는 최종 반환용 포인터

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1): # enumerate(s, 1)에서 1은 인덱스를 1부터 시작하겠다는 것. 슬라이싱의 인덱스 지정 때문.
            if need[char] > 0:
                missing -= 1
            # 참고로 위의 표현은 missing -= need[char] > 0 과 같다.
            need[char] -= 1

            if missing == 0: # 필요한 문자가 모두 윈도우에 들어왔고
                # left 포인터의 문자가 불필요(-1)하다면 left 포인터를 오른쪽으로 이동(좁힌다)한다.
                # missing이 0이 된 시점에서 right의 문자는 타겟이지만 left는 아닐 수 있기 때문.
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if end == 0 or right - left <= end - start: # end 포인터가 아직 없거나(초기값이거나) 확인 포인터가 최종 포인터보다 작다면(윈도우가 좁아졌다면)
                    start, end = left, right # 최종 포인터를 갱신한다.
                
                # 더 작은 윈도우를 찾기 위해 left(현재 값은 타겟 문자 중 하나를 가리킴)를 한 칸 전진시킴.
                need[s[left]] += 1 # left에 해당하는 문자의 갯수를 다시 돌려 두고
                missing += 1 # left에 해당하는 문자는 타겟에 포함되므로 missing 역시 돌려 둠
                left += 1 # 마지막으로 left를 전진
        
        return s[start:end]

    def minWindow_counter(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            # AND 연산 결과로 왼쪽 포인터 이동 판단
            while current_count & t_count == t_count: # & 연산은 두 카운터의 교집합을 반환한다.
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1
                
        return s[start:end] if end - start <= len(s) else ''

sol = Solution()

s = "ADOBECODEBANC"
t = "ABC"
# print(s, t, sol.minWindow_bf(s, t))
# print(s, t, sol.minWindow_tp(s, t))
print(s, t, sol.minWindow_counter(s, t))

s = "a"
t = "a"
# print(s, t, sol.minWindow_bf(s, t))
# print(s, t, sol.minWindow_tp(s, t))
print(s, t, sol.minWindow_counter(s, t))

s = "a"
t = "aa"
# print(s, t, sol.minWindow_bf(s, t))
# print(s, t, sol.minWindow_tp(s, t))
print(s, t, sol.minWindow_counter(s, t))