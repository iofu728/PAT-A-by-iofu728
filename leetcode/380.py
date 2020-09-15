# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-15 12:07:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-15 12:08:37
"""
380. Insert Delete GetRandom O(1) Medium
Design a data structure that supports all following operations in average O(1) time.

 

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
Accepted 261,795 Submissions 547,886
"""
from random import choice
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.lists = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val] = len(self.lists)
        self.lists.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        last, idx = self.lists[-1], self.d[val]
        self.lists[idx], self.d[last] = last, idx
        self.lists.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.lists)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()