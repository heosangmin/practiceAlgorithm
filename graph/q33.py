'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
'''

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []

        def dfs(index, path):

            if len(digits) == len(path):
                result.append(path)
                return

            for char in dic[digits[index]]:
                dfs(index+1, path+char)

        dfs(0, "")

        return result


digits1 = "23"
digits2 = ""
digits3 = "2"

s = Solution()
print(s.letterCombinations(digits1))
print(s.letterCombinations(digits2))
print(s.letterCombinations(digits3))