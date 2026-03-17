"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

# Topics: Sliding Window, Hash Table, Set

# Approach: Sliding Window with Set
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(min(N, K)) for the sliding window set
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
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

# Approach: Hash Table to store last seen index of each number
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(N) in the worst case if all elements are unique
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                if i - seen[num] <= k:
                    return True
            seen[num] = i
        return False
