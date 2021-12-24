'''
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 104
- -104 <= nums[i] <= 104
'''

from typing import List
import collections
import heapq

class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        '''
        파이썬 heapq 모듈은 최소 힙만 지원하므로
        음수로 저장한 다음 가장 낮은 수부터 추출해 부호를 변환하면
        최대 힙처럼 동작하도록 구현할 수 있다.
        '''
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        '''
        heapq 모듈의 heapify()를 이용하면 리스트를 최소 힙으로 변환할 수 있다.
        변환한 힙에서 len() - k만큼 heappop으로 제거하고
        마지막으로 heappop()으로 반환한다.
        '''
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        '''
        heapq 모듈의 nlargest()는 n번째만큼 큰 값을 리스트로 리턴한다.
        '''
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        '''
        추가, 삭제가 빈번할 경우에는 heapq를 이용한 힙 정렬이 유용하지만
        입력값이 고정되어 있을 때는 한 번 정렬하는 것으로 충분하다.
        '''
        return sorted(nums, reverse=True)[k-1]

nums1 = [3,2,1,5,6,4]
k1 = 2

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4

s = Solution()

# print(s.findKthLargest1(nums1, k1))
# print(s.findKthLargest1(nums2, k2))

# print(s.findKthLargest2(nums1, k1))
# print(s.findKthLargest2(nums2, k2))

# print(s.findKthLargest3(nums1, k1))
# print(s.findKthLargest3(nums2, k2))

print(s.findKthLargest4(nums1, k1))
print(s.findKthLargest4(nums2, k2))