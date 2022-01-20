'''
15. 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 1. blute force
        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, len(nums) - 1):
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #         for k in range(j + 1, len(nums)):
        #             if k > j + 1 and nums[k] == nums[k - 1]:
        #                 continue
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 results.append([nums[i], nums[j], nums[k]])

        # 2. two pointer
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        
        return results

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))