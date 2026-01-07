"""
https://leetcode.com/problems/two-sum/
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

# Approach: Brute force
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Approach: Two pass Hash Table
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        size = len(nums)

        for i in range(size):
            seen[nums[i]] = i

        for i in range(size):
            wanted = target - nums[i]
            if wanted in seen and seen[wanted] != i:
                return [i, seen[wanted]]

        return []

# Approach: One pass Hash Table
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        size = len(nums)

        for i in range(size):
            wanted = target - nums[i]
            if wanted in seen:
                return [i, seen[wanted]]
            seen[nums[i]] = i

        return []
