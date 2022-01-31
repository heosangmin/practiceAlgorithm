'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        카데인 알고리즘이라고도 불림.(Kadane's Algorithm)
        > 최대 서브 배열을 찾기 위해 어디서 시작되는지를 찾는 문제 O(n^2) 풀이에서
        > 각 단계마다 최댓값을 담아 어디서 끝나는지를 찾는 문제 O(n) 풀이로 치환해서 풀이했다.
        '''
        sum_of_prev = max_sum = -10000
        for num in nums:
            sum_of_prev = max(num, sum_of_prev + num)
            max_sum = max(sum_of_prev, max_sum)
        return max_sum

    def maxSubArray_memoization(self, nums: List[int]) -> int:
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        return max(sums)

s = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(nums, s.maxSubArray(nums))
print(nums, s.maxSubArray_memoization(nums))

nums = [1]
# print(nums, s.maxSubArray(nums))
print(nums, s.maxSubArray_memoization(nums))

nums = [5,4,-1,7,8]
# print(nums, s.maxSubArray(nums))
print(nums, s.maxSubArray_memoization(nums))

nums = [1,2]
# print(nums, s.maxSubArray(nums))
print(nums, s.maxSubArray_memoization(nums))