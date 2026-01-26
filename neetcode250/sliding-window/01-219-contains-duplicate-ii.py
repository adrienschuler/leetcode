"""
https://leetcode.com/problems/contains-duplicate-ii/
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import List

# Topics: Sliding Window, Hash Table, Set

# Approach: Sliding Window with Set
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(min(N, K)) for the sliding window set
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False
