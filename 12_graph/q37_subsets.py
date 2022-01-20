'''
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
'''

from typing import List

class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        def dfs(index: int, path: List[int]):
            if index >= len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                results.append(path[:])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return results

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

nums1 = [1,2,3]
nums2 = [0]

s = Solution()
print(s.subsets1(nums1))
print(s.subsets1(nums2))
print(s.subsets2(nums1))
print(s.subsets2(nums2))