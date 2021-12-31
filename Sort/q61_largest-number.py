'''
179. Largest Number
https://leetcode.com/problems/largest-number/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
'''

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return nums
        
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            #while j >= 0 and nums[j] > key:
            while j >= 0 and str(nums[j]) + str(key) < str(key) + str(nums[j]):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        
        # 입력 값이 ["0","0"]인 경우가 있으므로 join() 결과를 int로 변환해 다시 str로 변환한다.
        return str(int("".join(map(str, nums))))

    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber_book(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int("".join(map(str, nums))))

nums1 = [10,2]
nums2 = [3,30,34,5,9]

s = Solution()

print(s.largestNumber(nums1))
print(s.largestNumber(nums2))

# print(s.largestNumber_book(nums1))
# print(s.largestNumber_book(nums2))