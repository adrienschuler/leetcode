"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
Easy

Given the root of a binary tree, invert the tree, and return its root.

Topics: Tree, DFS, BFS, Binary Tree
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach: recursive DFS
# Time complexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
# Space complexity: O(h) where h is the height of the tree, due to the recursion stack
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Approach: iterative BFS
# Time complexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
# Space complexity: O(w) where w is the maximum width of the tree, due to the queue storing nodes at each level.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        return root
