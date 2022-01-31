'''
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 
Constraints:
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

from typing import List
import bisect

class Solution:
    def twoSum_two_pointer(self, numbers: List[int], target: int) -> List[int]:
        '''
        O(n)
        '''
        left, right = 0, len(numbers) - 1
        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
    
    def twoSum_bs(self, numbers: List[int], target: int) -> List[int]:
        '''
        첫 번째 인덱스를 탐색하는 O(n)과
        두 번째 인덱스를 이진 탐색하는 O(log n)의 조합이므로
        O(n log n)으로 풀이 가능하다.
        '''
        for i, v in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            expected = target - v
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]

    def twoSum_bisect_slicing(self, numbers: List[int], target: int) -> List[int]:
        '''
        위의 twoSum_bs에서 이진 검색 부분을 bisect 모듈로 대체한다.
        하지만 슬라이싱이 성능에 부하를 준다.
        '''
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k + 1:], expected)
            if i < len(numbers[k + 1:]) and numbers[k + 1 + i] == expected:
                return [k + 1, k + 1 + i + 1]

    def twoSum_bisect_slicing_2(self, numbers: List[int], target: int) -> List[int]:
        '''
        슬라이싱 최소화
        '''
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[k + 1 + i] == expected:
                return [k + 1, k + 1 + i + 1]
    
    def twoSum_bisect_advanced(self, numbers: List[int], target: int) -> List[int]:
        '''
        bisect_left 함수 파라미터의 활용
        '''
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return [k + 1, i + 1]


s = Solution()

numbers = [2,7,11,15]
target = 9
#print(numbers, target, s.twoSum_two_pointer(numbers, target))
#print(numbers, target, s.twoSum_bs(numbers, target))
#print(numbers, target, s.twoSum_bisect_slicing(numbers, target))
#print(numbers, target, s.twoSum_bisect_slicing_2(numbers, target))
print(numbers, target, s.twoSum_bisect_advanced(numbers, target))

numbers = [2,3,4]
target = 6
#print(numbers, target, s.twoSum_two_pointer(numbers, target))
#print(numbers, target, s.twoSum_bs(numbers, target))
#print(numbers, target, s.twoSum_bisect_slicing(numbers, target))
#print(numbers, target, s.twoSum_bisect_slicing_2(numbers, target))
print(numbers, target, s.twoSum_bisect_advanced(numbers, target))

numbers = [-1,0]
target = -1
#print(numbers, target, s.twoSum_two_pointer(numbers, target))
#print(numbers, target, s.twoSum_bs(numbers, target))
#print(numbers, target, s.twoSum_bisect_slicing(numbers, target))
#print(numbers, target, s.twoSum_bisect_slicing_2(numbers, target))
print(numbers, target, s.twoSum_bisect_advanced(numbers, target))