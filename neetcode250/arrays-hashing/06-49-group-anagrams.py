"""
https://leetcode.com/problems/group-anagrams/
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

# Topics: Hash Table, String, Sorting

# Approach: Sort each string and use it as a key in a hash map
# Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string
# Space Complexity: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i, s in enumerate(strs):
            anagrams[''.join(sorted(s))].append(s)

        return list(anagrams.values())

# Approach: Frequency count as a key in a hash map
# Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
# Space Complexity: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a - z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())
