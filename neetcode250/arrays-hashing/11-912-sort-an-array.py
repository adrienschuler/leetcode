"""
https://leetcode.com/problems/sort-an-array/
Medium

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""

# Topics: Sorting, Divide and Conquer, Merge Sort, Bubble Sort

# TODO:
# Heap sort
# BST (Binary Search Tree)

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.bubbleSort(nums)
        # return self.insertionSort(nums)
        # return self.bucketSort(nums)
        return self.quickSort(nums)
        # return self.mergeSort(nums)

    # Approach: Bubble Sort
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Stable: Yes
    def bubbleSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            swapped = False

            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr

    # Approach: Insertion Sort
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Stable: Yes
    def insertionSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(1, n):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                else:
                    break
        return arr

    # Approach: Bucket Sort
    # Time complexity: O(n + k) where n is number of elements and k is number of buckets
    # Space complexity: O(n + k) for the buckets
    # Stable: Yes
    def bucketSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        buckets = [[] for _ in range(n)]

        for num in arr:
            # TODO: Handle negative numbers
            bi = int(n * num)
            buckets[bi].append(num)

        for bucket in buckets:
            self.insertionSort(bucket)

        i = 0
        for bucket in buckets:
            for num in bucket:
                arr[i] = num
                i += 1

        return arr

    # Approach: Quick Sort (Divide and Conquer)
    # Time complexity: O(n log n) on average, O(n^2) in the worst case
    # Space complexity: O(log n) due to recursion stack
    # Stable: No
    def quickSort(self, arr: List[int]) -> List[int]:
        return self.quickSortHelper(arr, 0, len(arr) - 1)

    def quickSortHelper(self, arr: List[int], low: int, high: int) -> List[int]:
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSortHelper(arr, low, pi - 1)
            self.quickSortHelper(arr, pi + 1, high)
        return arr

    def partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Approach: Using list comprehensions
    def _quickSort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1: return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return self._quickSort(left) + [pivot] + self._quickSort(right)

    # Approach: Merge Sort (Divide and Conquer)
    # Time complexity: O(n log n) Divide step takes O(log n) and Merge step takes O(n)
    # Space complexity: O(n) because of the extra arrays created during the merge process (not in-place)
    # Stable: Yes
    def mergeSort(self, arr: List[int]) -> List[int]:
        print("mergeSort:", arr)
        n = len(arr)
        if n == 1: return arr
        m = n // 2
        L = self.mergeSort(arr[:m])
        R = self.mergeSort(arr[m:])

        return self.mergeSortedArrays(L, R)

    def mergeSortedArrays(self, L: List[int], R: List[int]) -> List[int]:
        print("mergeSortedArrays:", L, R)
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


def main() -> None:
    solution = Solution()

    # nums = [5, 2, 3, 1]
    # print(solution.sortArray(nums))  # [1, 2, 3, 5]

    nums = [5, 1, 1, 2, 0, 0]
    print(solution.sortArray(nums))  # [0, 0, 1, 1, 2, 5]


if __name__ == "__main__":
    main()
