"""
https://leetcode.com/problems/sort-colors/
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
"""

# Topics: Two Pointers, Array

# Approach: Dutch National Flag Algorithm
# Aka 3-way partitioning
# or Quick sort partitioning
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1

            i += 1
