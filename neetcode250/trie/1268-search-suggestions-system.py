"""
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
Medium

You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character
of searchWord is typed. Suggested products should have a common prefix with searchWord.
If there are more than three products with a common prefix, return the three lexicographically
minimum products.

Return a list of lists of the suggested products after each character of searchWord is typed.
"""

from typing import List

# Topics: Array, String, Binary Search, Trie, Sorting

# Approach: Trie (Prefix Tree) — store up to 3 words per node at insert time (sorted)
# Time: insert O(n log n) where n is the number of products (due to sorting), search O(m) where m is the length of searchWord
# Space: O(m) where m is the total number of characters in all products


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # up to 3 lexicographically smallest words through this node


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self._index(products)
        return self._suggest(searchWord)

    def _index(self, products: List[str]) -> None:
        self.root = TrieNode()
        for word in sorted(products):
            cur = self.root
            for char in word:
                cur = cur.children.setdefault(char, TrieNode())
                if len(cur.words) < 3:
                    cur.words.append(word)

    def _suggest(self, searchWord: str) -> List[List[str]]:
        suggestions = []
        cur = self.root
        for char in searchWord:
            cur = cur.children.get(char) if cur else None
            suggestions.append(cur.words if cur else [])
        return suggestions


search = Solution()

assert search.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse") == [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
assert search.suggestedProducts(["havana"], "havana") == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
