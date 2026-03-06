"""
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

from collections import Counter
from typing import List


# Approach: hash map
# Time: O(n + m) or O(min(n, m)) if we count freqs on smaller list
# Space: O(n)
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    inter = []

    # 1. count freqs on smallest list (saves time and space)
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    freqs = Counter(nums1)

    # 2. iterate through nums2 build up inter
    for num in nums2:
        if freqs[num] and freqs[num] > 0:
            inter.append(num)
            freqs[num] -= 1
    return inter

# Approach: two pointers (requires sorted input)
# Time: O(n + m)
# Space: O(1)
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    inter = []
    l = r = 0

    while l < len(nums1) and r < len(nums2):
        if nums1[l] == nums2[r]:
            inter.append(nums1[l])
            l, r = l + 1, r + 1
        elif nums1[l] < nums2[r]:
            l += 1
        else:
            r += 1

    return inter

assert intersection([1,1,2,2], [2,2]) == [2,2]
assert intersection([4,5,9], [4,4,8,9,9]) == ([4,9] or [9,4])
