"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Medium

Given a string s, find the length of the longest substring without duplicate characters.
"""

# Topics: Hash Map, Sliding Window, String

# Approach: Sliding window with hash map
# Time Complexity: O(n)
# Space Complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_index = {}
        longest = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= l:
                l = char_index[char] + 1
            char_index[char] = i
            longest = max(longest, i - l + 1)

        return longest
