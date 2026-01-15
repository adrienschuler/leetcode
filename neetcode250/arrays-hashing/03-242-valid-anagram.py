"""
https://leetcode.com/problems/valid-anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

# Topics: Hash Table, String, Sorting

# Approach: Frequency Counter
# Time Complexity: O(n)
# Space Complexity: O(1) - since the character set is limited
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        for char in t:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
            else:
                return False

        return True
