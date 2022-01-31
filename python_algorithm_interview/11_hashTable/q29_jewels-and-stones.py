'''
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0
'''

import collections


class Solution:
    def numJewelsInStones1(self, jewels: str, stones: str) -> int:
        d = {}
        for jewel in jewels:
            if jewel not in d:
                d[jewel] = 0

        for stone in stones:
            if stone in d:
                d[stone] += 1
        
        sum = 0
        for char in d:
            sum += d[char]
        
        return sum

    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        
        for stone in stones:
            freqs[stone] += 1
        
        for jewel in jewels:
            if jewel in freqs:
                count += freqs[jewel]
        
        return count

    def numJewelsInStones3(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for jewel in jewels:
            if jewel in freqs:
                count += freqs[jewel]
        
        return count

    def numJewelsInStones4(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)

solution = Solution()

jewels1 = "aA"
stones1 = "aAAbbbb"
jewels2 = "z"
stones2 = "ZZ"
print(solution.numJewelsInStones1(jewels1, stones1))
print(solution.numJewelsInStones2(jewels1, stones1))
print(solution.numJewelsInStones3(jewels1, stones1))
print(solution.numJewelsInStones4(jewels1, stones1))