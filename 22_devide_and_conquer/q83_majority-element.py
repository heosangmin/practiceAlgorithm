'''
169. Majority Element
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
'''
from typing import List
import collections

class Solution:
    def majorityElement_bf(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) > len(nums) // 2:
                return n

    def majorityElement_dynamic(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num

    def majorityElement_dq(self, nums: List[int]) -> int:
        '''
        분할 정복으로 풀 수 있다니 신기하다. 굳이?라는 느낌이지만.
        이 풀이의 장점은 탐색 시간이 O(n log n)에 가깝다는 것이다.

        마지막 리턴 부분이 억지스럽달까. 쉽게 풀어 써도 될텐데 굳이?라는 느낌이다.
        return [b,a][nums.count(a) > len(nums) // 2] 에서
        인덱스를 구하는 식이 bool의 결과를 내는데 True는 1을, False는 0임을 보여준다.

        아무리 생각해도 이 책은 저자 잘난 맛...이 너무 느껴진다.
        풀이도 대부분 그냥 코드 설명에서 크게 벗어나지 않는다. 접근 방법과 원리를 말해주면 좋을텐데.
        파이썬으로 알고리즘 문제을 경험할 수 있는 좋은 책이지만 썩 유쾌하지는 않다.
        스스로 생각할 수 있도록 유도하지 않고 자기의 풀이만 보여준다.
        '''
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement_dq(nums[:half])
        b = self.majorityElement_dq(nums[half:])

        return [b, a][nums.count(a) > half]

    def majorityElement_pythonic(self, nums: List[int]) -> int:
        '''
        정렬한 리스트의 가운데 값은 과반수에 해당하는 값이므로.
        '''
        return sorted(nums)[len(nums) // 2]

s = Solution()

nums = [3,2,3]
# print(nums, s.majorityElement_bf(nums))
# print(nums, s.majorityElement_dynamic(nums))
# print(nums, s.majorityElement_dq(nums))
print(nums, s.majorityElement_pythonic(nums))

nums = [2,2,1,1,1,2,2]
# print(nums, s.majorityElement_bf(nums))
# print(nums, s.majorityElement_dynamic(nums))
# print(nums, s.majorityElement_dq(nums))
print(nums, s.majorityElement_pythonic(nums))