"""
https://leetcode.com/problems/binary-search
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""

# Topics: Array, Binary Search

# Approach: Iterative Binary Search
# Time Complexity: O(log N) where N is the length of nums
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1
