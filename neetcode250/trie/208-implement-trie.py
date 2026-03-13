"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
and retrieve keys in a dataset of strings. Implement the Trie class:
- Trie() initializes the trie object.
- void insert(String word) inserts the string word into the trie.
- boolean search(String word) returns true if the string word is in the trie, false otherwise.
- boolean startsWith(String prefix) returns true if there is a previously inserted string that
  has the prefix prefix, and false otherwise.
"""

# Topics: Hash Table, String, Design, Trie


# Approach: Trie (Prefix Tree)
# Time:  insert O(n), search O(n), startsWith O(n) where n is the length of the word/prefix
# Space: O(n) where n is the total number of characters in all words inserted
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
