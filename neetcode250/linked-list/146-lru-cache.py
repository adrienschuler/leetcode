"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise,
  add the key-value pair to the cache. If the number of keys exceeds the capacity from
  this operation, evict the least recently used key.

Both get and put must run in O(1) average time complexity.

Topics: Hash Table, Linked List, Design, Doubly-Linked List
"""

class Node:
    def __init__(self, key: int, val: int, prev = None, nxt = None) -> None:
        self.key, self.val = key, val
        self.prev, self.next = prev, nxt

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def evict(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.evict(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.evict(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.evict(lru)
            del self.cache[lru.key]

cache = LRUCache(2)

assert cache.put(1, 1) == None
assert cache.put(2, 2) == None
assert cache.get(1) == 1
assert cache.put(3, 3) == None
assert cache.get(2) == -1
assert cache.put(4, 4) == None
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
