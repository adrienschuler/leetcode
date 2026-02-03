"""
https://leetcode.com/problems/product-of-array-except-self/
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""

# Topics: Array, Prefix Sum

# Approach: Prefix and Postfix Products
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1) excluding the output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
