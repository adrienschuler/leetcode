"""
https://leetcode.com/problems/contains-duplicate/
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# Topics: Array, Hash Table

# Approach: Hash Set
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
