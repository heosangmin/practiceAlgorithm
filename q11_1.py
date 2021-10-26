'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            answer.append(p)
        p = 1
        for i in range(len(nums)-2,-1,-1):
            p *= nums[i + 1]
            answer[i] *= p
        return answer


nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
solution = Solution()
print(solution.productExceptSelf(nums1))
print(solution.productExceptSelf(nums2))