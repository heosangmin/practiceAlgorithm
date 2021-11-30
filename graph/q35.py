'''
77. Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Input: n = 1, k = 1
Output: [[1]]
 
Constraints:
- 1 <= n <= 20
- 1 <= k <= n
'''

from typing import List
import itertools

class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
        result = []
        elements = []

        def dfs(start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(i+1, k-1)
                elements.pop()
            
            
        dfs(1, k)
        return result
            

    def combine2(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements: List, start: int, k: int):
            if k == 0:
                results.append(elements[:])
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        return results

    def combine3(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, itertools.combinations(range(1, n+1), k)))

n1 = 4
k1 = 2
n2 = 1
k2 = 1
n3 = 5
k3 = 3

s = Solution()
print(s.combine1(n1, k1))
print(s.combine1(n2, k2))
print(s.combine1(n3, k3))

print(s.combine2(n1, k1))
print(s.combine2(n2, k2))
print(s.combine2(n3, k3))

print(s.combine3(n1, k1))
print(s.combine3(n2, k2))
print(s.combine3(n3, k3))