"""
https://leetcode.com/problems/valid-palindrome/
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# Topics: Two Pointers, String

# Approach: Use two pointers to compare characters from both ends after cleaning the string
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]
