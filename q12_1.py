'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0
'''

from typing import List
import sys

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # 1. blute force
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit

solution = Solution()
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
print(solution.maxProfit1(prices1))
print(solution.maxProfit1(prices2))
print(solution.maxProfit2(prices1))
print(solution.maxProfit2(prices2))