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
"""

# Topics: Hash Table

# Approach: Brute force using a list
# Time Complexity: O(n) for add, remove, and contains
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

# TODO: Implement a more efficient version
