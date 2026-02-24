"""
https://leetcode.com/problems/longest-common-prefix/
Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

# Topics: Array, String

# Approach: Vertical Scanning with Shortest String
# Time Complexity: O(m * n) where m is the length of the shortest string and n is the number of strings
# Space Complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]
        return shortest


# Approach: Vertical Scanning
# Time Complexity: O(m * n) where m is the length of the first string and n is the number of strings
# Space Complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if len(s) == i or s[i] != c:
                    return prefix
            prefix += c
        return prefix
