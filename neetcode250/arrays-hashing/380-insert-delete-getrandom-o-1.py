"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1
Medium

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            i = self.map[val]
            last_val = self.list[-1]
            self.list[i] = last_val
            self.list.pop()
            self.map[last_val] = i
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)

randomizedSet = RandomizedSet()
assert randomizedSet.insert(1) == True # 1 was inserted successfully.
assert randomizedSet.remove(2) == False # 2 does not exist in the set.
assert randomizedSet.insert(2) == True
assert randomizedSet.getRandom() in [1, 2]
assert randomizedSet.remove(1) == True # Set now contains [2].
assert randomizedSet.insert(2) == False # 2 was already in the set
assert randomizedSet.getRandom() == 2 # 2 is the only number in the set
