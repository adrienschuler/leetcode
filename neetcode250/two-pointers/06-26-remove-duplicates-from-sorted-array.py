"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
"""

# Topics: Two Pointers, Array

# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l
