"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/description/
Easy
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

# Topics: Two Pointers, String

# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n): for the substring slices - can be optimized to O(1) by using helper function with indices
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r] and not skipL:
                skipL, skipR = s[l + 1:r + 1], s[l:r] # TODO: understand slices
                return (skipL == skipL[::-1]
                        or skipR == skipR[::-1])
            l, r = l + 1, r - 1

        return True

# Approach: Two Pointers with Helper Function
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            l, r = l + 1, r - 1
        return True
