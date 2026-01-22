"""
https://leetcode.com/problems/sort-an-array/
Medium

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""

# Topics: Sorting, Divide and Conquer, Merge Sort, Bubble Sort

# Approach: Bubble Sort
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bubbleSort(nums)

    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums

    def mergeSortedArrays(self, L: List[int], R: List[int]) -> List[int]:
        l = r = i = 0
        L_len, R_len = len(L), len(R)
        sorted_arr = [0] * (L_len + R_len)

        while l < L_len and r < R_len:
            if L[l] < R[r]:
                sorted_arr[i] = L[l]
                l += 1
            else:
                sorted_arr[i] = R[r]
                r += 1
            i += 1

        while l < L_len:
            sorted_arr[i] = L[l]
            l, i = l + 1, i + 1
        while r < R_len:
            sorted_arr[i] = R[r]
            r, i = r + 1, i + 1

        return sorted_arr

    # Approach: Merge Sort (Divide and Conquer)
    # Time complexity: O(n log n)
    # Space complexity: O(n) because of the extra arrays created during the merge process (not in-place)
    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) == 1: return arr
        m = len(arr) // 2
        L = self.mergeSort(arr[:m])
        R = self.mergeSort(arr[m:])

        return self.mergeSortedArrays(L, R)


# TODO:
# Quick sort
# Heap sort
# BST (binary search tree)
