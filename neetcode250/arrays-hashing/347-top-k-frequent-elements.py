"""
347. Top K Frequent Elements
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
        freqs = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[freq])
            if len(result) >= k:
                return result[:k]

# Approach: Heap
# Time Complexity: O(n log k)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        hq = []

        for num, freq in counts.items():
            heapq.heappush(hq, (freq, num))
            if len(hq) > k:
                heapq.heappop(hq)

        return [num for _, num in hq]

    assert topKFrequent(nums=[1,2,3,4,4,5,2,2], k=2) == [2, 4]
