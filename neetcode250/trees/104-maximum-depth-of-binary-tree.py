"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Topics: Tree, DFS, BFS, Binary Tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach: recursive DFS
# Time complexity: O(n) where n is the number of nodes in the tree, since we visit each node once
# Space complexity: O(h) where h is the height of the tree, due to the recursion stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Approach: iterative DFS
# Time complexity: O(n) where n is the number of nodes in the tree, since we visit each node once
# Space complexity: O(h) where h is the height of the tree, due to the stack storing nodes along the path from the root to the current node
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        level = 0
        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return level

# Approach: iterative BFS
# Time complexity: O(n) where n is the number of nodes in the tree, since
# we visit each node once
# Space complexity: O(w) where w is the maximum width of the tree, due to the queue storing nodes at each level
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

