'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        네덜란드 국기 문제(https://en.wikipedia.org/wiki/Dutch_national_flag_problem)의 수도코드 참조
        """
        i = 0
        j = 0
        k = len(nums) - 1
        
        while j <= k:
            if nums[j] < 1: # mid=1
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1: # mid=1
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1        


nums1 = [2,0,2,1,1,0]
nums2 = [2,0,1]

s = Solution()

print(nums1)
s.sortColors(nums1)
print(nums1)

print(nums2)
s.sortColors(nums2)
print(nums2)