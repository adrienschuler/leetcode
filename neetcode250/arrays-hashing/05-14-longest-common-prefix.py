"""
https://leetcode.com/problems/longest-common-prefix/
Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

# Vertical Scanning
# Time Complexity: O(S) where S is the sum of all characters in all strings
# Space Complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i, c in enumerate(shortest):
            for string in strs:
                if string[i] != c:
                    return shortest[:i]

        return shortest
