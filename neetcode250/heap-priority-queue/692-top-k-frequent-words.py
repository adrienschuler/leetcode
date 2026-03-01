"""
692. Top K Frequent Words
Medium
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""

# Topics: Hash Map, Heap (Priority Queue), Sorting


# Approach: Heap
# Time Complexity: O(n log k)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        hq = []

        for word, freq in counts.items():
            heapq.heappush(hq, (-freq, word))

        return [heapq.heappop(hq)[1] for _ in range(k)]
