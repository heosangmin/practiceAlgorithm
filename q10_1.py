'''
561. Array Partition I
https://leetcode.com/problems/array-partition-i/

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Input: nums = [1,4,3,2]
Output: 4

Input: nums = [6,2,6,5,1,2]
Output: 9
'''

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))
print(solution.arrayPairSum([6,2,6,5,1,2]))