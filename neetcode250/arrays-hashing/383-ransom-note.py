"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine, and false otherwise.
Each letter in magazine can only be used once.
"""

# Topics: Hash Table, String, Counting

# Approach: Frequency counting with a hash table.
# Time:  O(n + m) where n is the length of ransomNote and m is the length of magazine
# Space: O(m) for the Counter
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqs = Counter(magazine)
        for char in ransomNote:
            if char in freqs and freqs[char] > 0:
                freqs[char] -= 1
            else:
                return False
        return True
