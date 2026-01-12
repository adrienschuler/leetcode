"""
https://leetcode.com/problems/majority-element/
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

# Approach: Frequency Counter
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        total = len(nums)

        for num in nums:
            seen[num] += 1
            if seen[num] >= (total / 2):
                return num
        return -1

# Approach: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
