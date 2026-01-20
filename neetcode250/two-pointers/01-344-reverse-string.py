"""
https://leetcode.com/problems/reverse-string/
Easy
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

# Topics: Two Pointers, String, Array

# Approach: Two Pointers, in-place swap
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1

# Approach: Recursion
# Time Complexity: O(n)
# Space Complexity: O(n) (function call stack)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                return reverse(l + 1, r - 1)
        return reverse(0, len(s) - 1)
