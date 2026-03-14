"""
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/
Medium

Design a data structure that supports adding new words and finding if a string matches any
previously added string. '.' can match any letter.

- WordDictionary() initializes the object.
- void addWord(word) adds word to the data structure.
- bool search(word) returns true if there is any string in the data structure that matches word,
  where '.' matches any letter.
"""

# Topics: String, Depth-First Search, Design, Trie


# Approach: Trie + DFS
# Time:  addWord O(n), search O(m * 26^k) where n is the length of the word, m is the length of the search word, and k is the number of '.' in the search word
# Space: O(n) for the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    # Backtracking DFS
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.word
            char = word[i]
            if char != '.':
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
            else:
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
        return dfs(self.root, 0)

    # alternative BFS with a set of current nodes
    # Time: O(m * 26^k) where m is the length of the search word, and k is the number of '.' in the search word
    # Technically slower, BFS always explores all live paths before returning, while DFS can return early if it finds a match
    # Space: O(26^k) for the set of current nodes
    def search(self, word: str) -> bool:
        current = {self.root}

        for char in word:
            nxt = set()
            for node in current:
                if char == '.':
                    nxt |= set(node.children.values())
                elif char in node.children:
                    nxt.add(node.children[char])
            current = nxt

        return any(node.word for node in current)
