"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
Medium

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

# Topics: Stack, Monotonic Stack

# Approach: Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        indices = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while indices and temp > temperatures[indices[-1]]:
                j = indices.pop()
                output[j] = i - j
            indices.append(i)
        return output
