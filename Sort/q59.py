'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for item in sorted(intervals, key=lambda x: x[0]):
            if merged and merged[-1][1] >= item[0]:
                # 내 풀이
                # merged의 대상 아이템의 0번째 값은 변하지 않으므로
                # merged[-1][1]의 값만 변경하면 되겠다.
                #merged[-1] = [merged[-1][0], max(merged[-1][1],item[1])]

                # 책 풀이
                merged[-1][1] = max(merged[-1][1],item[1])
            else:
                merged.append(item)

                # 참고로, 책 풀이에는 merged += i, 라는 연산이 있다.
                # 콤마(,) 연산자인데 다음 예를 보자.
                # a,b = [1],[2,3]
                # a += b -> [1,2,3] 으로 concat 연산이다.
                # a += b, -> [1,[2,3]] 으로 b를 하나의 아이템으로서 추가해 중첩 리스트로 만들어준다.
                # 이것은 다시 말해 a += [b]와 같다.
                # 그냥 리스트 append해도 되는데 책에선 왜 굳이 이렇게 했는지 모르겠다. 이런 연산자도 있다는 거겠지.
        return merged

s = Solution()

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
intervals3 = [[1,4],[2,3]]

print(s.merge(intervals1))
print(s.merge(intervals2))
print(s.merge(intervals3))