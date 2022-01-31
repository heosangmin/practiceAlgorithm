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
        # 1. blute force
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # 2. using "in"
        # for i, n in enumerate(nums):
        #     complement = target - n
        #     if complement in nums[i+1:]:
        #         return [i,nums[i+1:].index(complement) + (i+1)]

        # 3. using dict 2
        # dict = {}
        # for i, n in enumerate(nums):
        #     dict[n] = i
        # for i, n in enumerate(nums):
        #     if (target - n) in dict:
        #         return [i, dict[target - n]]

        # 4. using dict 2 
        # dict = {}
        # for i,n in enumerate(nums):
        #     if target - n in dict:
        #         return [i, dict[target - n]]
        #     dict[n] = i

        # 5. two pointer (assumed the elements are sorted)
        left, right = 0, len(nums) - 1
        while left != right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [left,right]

solution = Solution()
print(solution.twoSum([2,7,11,15],9))