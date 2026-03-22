"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Topics: Tree, DFS, BST, Binary Tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach: DFS with bounds
# Time: O(n) where n is the number of nodes in the tree
# Space: O(h) where h is the height of the tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))


# Approach: Inorder traversal (iterative), track previous value
# A valid BST produces strictly increasing values in inorder traversal.
# Time: O(n)
# Space: O(h)
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float("-inf")
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val <= prev:
                return False
            prev = curr.val
            curr = curr.right

        return True
