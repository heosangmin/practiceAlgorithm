'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []

Input: candidates = [1], target = 1
Output: [[1]]

Input: candidates = [1], target = 2
Output: [[1,1]]
'''

from typing import List

class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        temp_list = []

        def dfs(start: int):
            if sum(temp_list) == target:
                results.append(temp_list[:])
                return
            
            if sum(temp_list) > target:
                return
            
            for index in range(start, len(candidates)):
                temp_list.append(candidates[index])
                dfs(index)
                temp_list.pop()

        dfs(0)
        return results

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result

candidates1 = [2,3,6,7]
target1 = 7
candidates2 = [2,3,5]
target2 = 8
candidates3 = [2]
target3 = 1
candidates4 = [1]
target4 = 1
candidates5 = [1]
target5 = 2

s = Solution()
print(s.combinationSum1(candidates1, target1))
print(s.combinationSum1(candidates2, target2))
print(s.combinationSum1(candidates3, target3))
print(s.combinationSum1(candidates4, target4))
print(s.combinationSum1(candidates5, target5))

print(s.combinationSum2(candidates1, target1))
print(s.combinationSum2(candidates2, target2))
print(s.combinationSum2(candidates3, target3))
print(s.combinationSum2(candidates4, target4))
print(s.combinationSum2(candidates5, target5))