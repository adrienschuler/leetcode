"""
https://leetcode.com/problems/top-k-frequent-elements/
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

# Topics: Hash Map, Heap (Priority Queue), Bucket Sort, Counting

# Approach: Bucket Sort
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res
