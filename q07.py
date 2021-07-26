'''
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # 2
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in nums[i+1:]:
        #         return [nums.index(num), nums[i+1:].index(complement) + (i+1)]

        # 3
        # nums_map = {}
        # for i, num in enumerate(nums):
        #     nums_map[num] = i
        # for i, num in enumerate(nums):
        #     if target - num in nums_map and i != nums_map[target-num]:
        #         return [nums.index(num), nums_map[target-num]]

        #4
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

solution = Solution()
print(solution.twoSum([2,7,11,15],9))