'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''

from typing import List
import bisect

class Solution:
    def intersection_bf(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        브루트 포스 풀이
        O(n^2)
        '''
        result = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)
        return list(result)

    def intersection_bisect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        이진 검색 풀이
        O(n log n)
        한쪽 배열에 이진 검색으로 탐색하면 효율이 올라갈 것임.
        이진 검색을 위해 대상 배열을 정렬하는 것을 잊지 말것.
        그리고 bisect_left 함수의 리턴 값의 특징을 알 것.
        찾는 요소의 인덱스를 리턴하는 것은 맞는데
        찾는 요소가 없다면 그 요소가 위치해야할 곳의 인덱스를 리턴함.
        a = [1,2,3]일 경우,
        bisect_left(a,0)은 0을 리턴함.
        bisect_left(a,4)는 3을 리턴함.
        bisect_left(a,2.5)는 2를 리턴함.
        '''
        result = set()
        nums2.sort()
        for n1 in nums1:
            i1 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i1 and n1 == nums2[i1]:
                result.add(n1)
        
        return list(result)
    
    def intersection_two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        
        return result

s = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
#print(nums1, nums2, s.intersection_bf(nums1, nums2))
#print(nums1, nums2, s.intersection_bisect(nums1, nums2))
print(nums1, nums2, s.intersection_two_pointer(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
#print(nums1, nums2, s.intersection_bf(nums1, nums2))
#print(nums1, nums2, s.intersection_bisect(nums1, nums2))
print(nums1, nums2, s.intersection_two_pointer(nums1, nums2))