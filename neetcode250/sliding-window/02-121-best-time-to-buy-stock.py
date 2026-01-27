"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# Topics: Two Pointers

# Approach: Sliding Window
# Time Complexity: O(N) where N is the length of prices
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = maxP = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r

        return maxP
