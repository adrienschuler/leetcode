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
    def __init__(self, key: int = -1, value: int = -1, prev = None, nxt = None):
        self.key, self.value = key, value
        self.prev, self.next = prev, nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru, self.mru = Node(), Node()
        self.lru.next, self.mru.prev = self.mru, self.lru

    def _evict(self, node: Node) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next

    def _insert(self, node: Node) -> None:
        node.next = self.mru
        node.prev = self.mru.prev
        node.prev.next = node
        self.mru.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._evict(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._evict(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self._evict(lru)
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
