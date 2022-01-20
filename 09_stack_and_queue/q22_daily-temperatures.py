'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for (i,temperature) in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                lastIndex = stack.pop()
                answer[lastIndex] = i - lastIndex
            stack.append(i)

        return answer

solution = Solution()

temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]
print(solution.dailyTemperatures(temperatures1))
print(solution.dailyTemperatures(temperatures2))
print(solution.dailyTemperatures(temperatures3))