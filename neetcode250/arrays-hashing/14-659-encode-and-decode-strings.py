"""
https://neetcode.io/problems/string-encode-and-decode
Medium

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""


# Topics: Two Pointers, String

class Solution:

    # Approach: Length Prefixing
    # Time Complexity: O(N) where N is the total length of all strings
    # Space Complexity: O(N) for the encoded string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res
