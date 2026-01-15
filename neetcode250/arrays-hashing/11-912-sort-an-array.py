"""
https://leetcode.com/problems/sort-an-array/
Medium

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""

# Topics: Sorting, Divide and Conquer, Array

# Approach: Bubble Sort
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bubbleSort(nums)

    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            flag = True

            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = False

            if flag:
                break

        return nums
