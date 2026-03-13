"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element.
You must write an algorithm that runs in O(log n) time.
"""

# Topics: Array, Binary Search

# Approach: Binary search — if mid > right, minimum is in the right half; else left half
# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def findMin(self, nums: list[int]) -> int:
        pass
