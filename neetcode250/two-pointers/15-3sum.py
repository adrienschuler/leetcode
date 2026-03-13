"""
3. 3Sum
https://leetcode.com/problems/3sum/
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.
"""

# Topics: Array, Two Pointers, Sorting

# Approach: Sort + fix one element, then use two pointers for the remaining pair
# Time Complexity: O(n^2)
# Space Complexity: O(1) excluding output
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pass
