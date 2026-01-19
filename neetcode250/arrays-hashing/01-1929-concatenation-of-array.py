"""
https://leetcode.com/problems/concatenation-of-array/
Easy

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

# Topics: Arrays

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            nums.append(nums[i])
        return nums

# Pythonic way
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n * 2)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
