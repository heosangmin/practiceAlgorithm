'''
46. Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.
'''

from typing import List
import itertools

class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:

        result = []
        prev_elements = []

        def dfs(nums: List[int]):
            if not nums:
                result.append(prev_elements[:])
                return

            for i in nums:
                new_nums = nums.copy()
                new_nums.remove(i)
                prev_elements.append(i)
                dfs(new_nums)
                prev_elements.pop()

        dfs(nums)
        
        return result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))

nums1 = [1,2,3]
nums2 = [0,1]
nums3 = [1]

s = Solution()
# print(s.permute1(nums1))
# print(s.permute1(nums2))
# print(s.permute1(nums3))
print(s.permute2(nums1))
print(s.permute2(nums2))
print(s.permute2(nums3))