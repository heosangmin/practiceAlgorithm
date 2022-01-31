'''
704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
'''

from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        일반적인 이진 검색 그대로 풀이
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            # mid = (left + right) // 2 # left + right는 자료형을 초과할 수도 있음.

            # 자료형을 초과하지 않는 중앙 위치 계산
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
    
    def search_recursive(self, nums: List[int], target: int) -> int:
        '''
        책에 나온 재귀 풀이
        '''
        def binary_search(left, right):
            if left <= right:
                # mid = (left + right) // 2 # left + right는 자료형을 초과할 수도 있음.

                # 자료형을 초과하지 않는 중앙 위치 계산
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1
        
        return binary_search(0, len(nums) - 1)

    def search_bisect(self, nums: List[int], target: int) -> int:
        '''
        책에 나온 이진 검색 모듈 풀이
        '''
        index = bisect.bisect_left(nums, target)
        
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def search_no_bs(self, nums: List[int], target: int) -> int:
        '''
        이진 검색이 아닌 index 함수로 찾기.
        책에서 말하고자 하는 것은 index()는 처음부터 순차적으로 검색하므로 O(n)이고 이진 검색은 O(log n)이다.
        찾고자 하는 값이 배열에서 비교적 앞쪽에 위치할 경우에는 index()가 더 빠를 수 있지만
        반대로 찾고자 하는 값이 뒤쪽에 있을 경우 심하게는 천 배 이상의 속도 차이로 이진 검색이 빠르다.
        즉 이진 검색은 일정한 속도로 값을 찾을 수 있다.
        '''
        try:
            return nums.index(target)
        except ValueError:
            return -1

nums1 = [-1,0,3,5,9,12]
target1 = 9
nums2 = [-1,0,3,5,9,12]
target2 = 2

s = Solution()

print(nums1, s.search(nums1, target1))
print(nums2, s.search(nums2, target2))

print(nums1, s.search_recursive(nums1, target1))
print(nums2, s.search_recursive(nums2, target2))

print(nums1, s.search_bisect(nums1, target1))
print(nums2, s.search_bisect(nums2, target2))

print(nums1, s.search_no_bs(nums1, target1))
print(nums2, s.search_no_bs(nums2, target2))