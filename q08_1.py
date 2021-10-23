'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

from typing import List

class Solution:
    def trap1(self, height: List[int]) -> int:

        # 1. blute force
        leftMaxList = [0]
        rightMaxList = [0]
        reversedHeight = height[::-1]
        
        for i in range(1,len(height)):
            if height[i-1] > leftMaxList[i-1]:
                leftMaxList.append(height[i-1])
            else:
                leftMaxList.append(leftMaxList[i-1])

            if reversedHeight[i-1] > rightMaxList[i-1]:
                rightMaxList.append(reversedHeight[i-1])
            else:
                rightMaxList.append(rightMaxList[i-1])
        
        rightMaxList = rightMaxList[::-1]
        
        sum = 0
        for i in range(0,len(height)):
            capacity = min(leftMaxList[i],rightMaxList[i]) - height[i]
            if capacity > 0:
                sum += capacity
        
        return sum

    def trap2(self, height: List[int]) -> int:
        # 2. two pointer
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        sum = 0
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                sum += left_max - height[left]
                left += 1
            else:
                sum += right_max - height[right]
                right -= 1
        return sum
        

height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap1(height))
print(solution.trap2(height))