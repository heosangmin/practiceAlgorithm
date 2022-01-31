'''
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''

from typing import List
import collections
import sys

class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        '''
        O(n*k)의 풀이인데 리트코드에서 실행하면 타임아웃이 발생하는 문제가 있다.
        '''
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i+k]))
        return result

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        '''
        역시 이 풀이도 타임아웃 발생
        '''
        result = []
        window = collections.deque()
        current_max = -sys.maxsize # 7장 198페이지의 최댓값 지정하는 법 참고하기(sys.maxsize 또는 float('-inf')등)
        for i, v in enumerate(nums):
            window.append(v)

            # 처음 윈도우 채우기
            if i < k - 1:
                continue
            
            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == -sys.maxsize:
                current_max = max(window)
            elif v > current_max:
                current_max = v

            result.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if window.popleft() == current_max:
                current_max = -sys.maxsize
        
        return result

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        '''
        https://github.com/onlybooks/algorithm-interview/issues/67
        위의 이슈를 참고
        '''
        result = []
        window = collections.deque() # 리스트의 값이 아닌 인덱스를 저장할 것임
        for i in range(len(nums)):

            # 윈도우 크기 유지를 위한 데크 요소 제거
            if window and i - window[0] == k:
                window.popleft()

            # window에 현재 추가하고자 하는 값보다 작은 값(의 인덱스)이 있다면 제거
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            # 윈도우에 현재 인덱스 추가
            window.append(i)

            # 결괏값 추가
            if i + 1 >= k:
                result.append(nums[window[0]])

        return result

s = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
# print(nums, k, s.maxSlidingWindow1(nums, k))
# print(nums, k, s.maxSlidingWindow2(nums, k))
print(nums, k, s.maxSlidingWindow3(nums, k))

nums = [1]
k = 1
# print(nums, k, s.maxSlidingWindow1(nums, k))
# print(nums, k, s.maxSlidingWindow2(nums, k))
print(nums, k, s.maxSlidingWindow3(nums, k))