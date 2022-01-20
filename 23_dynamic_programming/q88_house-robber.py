'''
198. House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
'''
from typing import List
import collections

class Solution:
    def rob_bf(self, nums: List[int]) -> int:
        '''
        풀이를 봐도 무슨 말인지 도무지 모르겠다. 무슨 소리를 하는 거야.
        다이나믹 프로그래밍으로 풀린다는 건, 중복되는 하위 문제가 있다는 건데
        리스트 값들을 특정 단위(i, i+1, i+2 등?)로 재귀 반복해서 구할 수 있다?
        '''
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            # a = _rob(i - 1)
            # b = _rob(i - 2)
            # n = nums[i]
            # print(f"i: {i}, (i - 1) = {a}, (i - 2) = {b}, nums[{i}] = {n}")
            return max(_rob(i - 1), _rob(i - 2) + nums[i])
            #return max(a, b + n)
        
        return _rob(len(nums) - 1)
    
    
    def rob_tabulation(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp.popitem()[1]

s = Solution()

nums = [1,2,3,1]
# print(nums, s.rob_bf(nums))
print(nums, s.rob_tabulation(nums))

nums = [2,7,9,3,1]
# print(nums, s.rob_bf(nums))
print(nums, s.rob_tabulation(nums))