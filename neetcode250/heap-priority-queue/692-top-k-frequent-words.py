"""
692. Top K Frequent Words
Medium
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""

# Topics: Hash Map, Heap (Priority Queue), Sorting


# Approach: sort
# Time:  O(n log n) where U is the number of unique words
# Space: O(U) where U is the number of unique words
class Solution:
    def topKFrequent(words: list, k: int) -> List:
        # Edge cases:
        # - what if k > len(words)
        # - ?

        # 1. count the frequencies of each words
        freqs = Counter(words)

        # 2. ensure we sort also the lexicographical order
        sorted_freqs = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))

        # 3. format the output
        # 4. slice the top k frequencies
        return [freqs[0] for freqs in sorted_freqs][:k]

# Approach: Heap
# Time Complexity: O(n log n) due to heap operations and sorting
# Space Complexity: O(n) for the heap and frequency map
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        hq = []

        for word, freq in counts.items():
            heapq.heappush(hq, (-freq, word))

        return [heapq.heappop(hq)[1] for _ in range(k)]
