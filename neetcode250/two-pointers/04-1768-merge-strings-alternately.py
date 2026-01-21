"""
https://leetcode.com/problems/merge-strings-alternately/description/
Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating
order, starting with word1. If a string is longer than the other, append the additional letters
onto the end of the merged string.
Return the merged string.
"""

# Topics: Two Pointers, String

# Approach: Two Pointers
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        l, r = 0, 0

        while l < len(word1) or r < len(word2):
            if l < len(word1):
                merged.append(word1[l])
                l += 1
            if r < len(word2):
                merged.append(word2[r])
                r += 1

        return "".join(merged)
