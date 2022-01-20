'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                waters = min( height[i], height[stack[-1]] ) - height[top]

                volume += distance * waters
            
            stack.append(i)
        
        return volume

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))