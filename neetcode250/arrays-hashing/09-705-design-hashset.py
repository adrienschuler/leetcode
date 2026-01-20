"""
https://leetcode.com/problems/design-hashset/
Easy

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)

Topics: Hash Table, Linked List

Intuition:
Handling collisions is the main challenge when designing a hash set.
"""

# Approach: Brute force using a simple list
# Time Complexity: Average O(n), Worst O(n)
# Space Complexity: O(n)
class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)
        return None

    def remove(self, key: int) -> None:
        for i in range(len(self.set)):
            if self.set[i] == key:
                del self.set[i]
                break
        return None

    def contains(self, key: int) -> bool:
        for num in self.set:
            if num == key:
                return True
        return False

# Approach: Hashing with Linked Lists (Chaining).
# Time Complexity: Average O(1), Worst O(n)
# Space Complexity: O(n)
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

"""
Other possible approaches:
- Hashing w/ Open Addressing:
    - Time Complexity: Average O(1), Worst O(n)
    - Space Complexity: O(n)
- Balanced BST
    - Time Complexity: O(log n)
    - Space Complexity: O(n)
"""
