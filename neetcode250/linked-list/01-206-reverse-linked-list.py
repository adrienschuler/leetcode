"""
https://leetcode.com/problems/reverse-linked-list/
Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Topics: Linked List, Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach: Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev

# Approach: Recursive
# Time Complexity: O(n)
# Space Complexity: O(n) - due to call stack
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                nxt = cur.next
                cur.next = prev
                return reverse(nxt, cur)

        return reverse(head, None)
